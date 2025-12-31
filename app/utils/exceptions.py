"""
异常处理模块
定义自定义异常类并注册全局错误处理器
"""
import traceback
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError as MarshmallowValidationError


class APIException(Exception):
    """基础 API 异常类"""
    status_code = 400
    message = '请求错误'
    
    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload
    
    def to_dict(self):
        """将异常转换为字典格式（兼容旧格式）"""
        rv = {
            'code': self.status_code,
            'msg': self.message
        }
        if self.payload:
            rv['data'] = self.payload
        return rv


class ValidationError(APIException):
    """数据验证错误"""
    status_code = 422
    message = '数据验证失败'


class NotFoundError(APIException):
    """资源未找到错误"""
    status_code = 404
    message = '资源未找到'


class UnauthorizedError(APIException):
    """未授权错误"""
    status_code = 401
    message = '未授权访问'


class ForbiddenError(APIException):
    """禁止访问错误"""
    status_code = 403
    message = '禁止访问'


def register_error_handlers(app: Flask):
    """注册全局错误处理器"""
    
    @app.errorhandler(APIException)
    def handle_api_exception(error: APIException):
        """处理自定义 API 异常"""
        response = jsonify({
            'code': error.status_code,
            'msg': error.message,
            'data': error.payload if error.payload else None
        })
        response.status_code = error.status_code
        return response
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(error: HTTPException):
        """处理 HTTP 异常"""
        return jsonify({
            'code': error.code,
            'msg': error.description or 'HTTP 错误'
        }), error.code
    
    @app.errorhandler(SQLAlchemyError)
    def handle_database_error(error: SQLAlchemyError):
        """处理数据库错误"""
        app.logger.error(f'Database error: {str(error)}')
        # 打印堆栈信息到日志
        app.logger.error(traceback.format_exc())
        return jsonify({
            'code': 500,
            'msg': '数据库操作失败'
        }), 500
    
    @app.errorhandler(MarshmallowValidationError)
    def handle_validation_error(error: MarshmallowValidationError):
        """处理 Marshmallow 参数校验错误"""
        app.logger.warning(f'Validation error: {str(error.messages)}')
        return jsonify({
            'code': 422,
            'msg': '参数校验失败',
            'data': error.messages
        }), 422
    
    @app.errorhandler(Exception)
    def handle_general_exception(error: Exception):
        """捕获所有未处理的异常，防止前端白屏"""
        # 打印完整的堆栈信息到日志
        app.logger.error(f'Unhandled exception: {str(error)}')
        app.logger.error(traceback.format_exc())
        
        # 返回友好的错误信息，不暴露内部错误详情
        return jsonify({
            'code': 500,
            'msg': 'Internal Server Error'
        }), 500
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """处理 404 错误"""
        return jsonify({
            'code': 404,
            'msg': '接口不存在'
        }), 404
    
    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        """处理 405 错误"""
        return jsonify({
            'code': 405,
            'msg': '请求方法不允许'
        }), 405

