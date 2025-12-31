"""
统一响应格式工具
提供标准化的 API 响应格式

标准 JSON 结构: {'code': 200, 'msg': 'success', 'data': ...}
"""
from flask import jsonify
from typing import Any, Dict, Optional


def success(data: Any = None, msg: str = 'success') -> tuple:
    """
    成功响应
    
    Args:
        data: 响应数据
        msg: 响应消息
    
    Returns:
        (response, status_code) 元组
    """
    response = {
        'code': 200,
        'msg': msg,
        'data': data
    }
    return jsonify(response), 200


def fail(code: int = 400, msg: str = '操作失败', data: Any = None) -> tuple:
    """
    失败响应
    
    Args:
        code: HTTP 状态码
        msg: 错误消息
        data: 额外的错误数据（可选）
    
    Returns:
        (response, status_code) 元组
    """
    response = {
        'code': code,
        'msg': msg
    }
    if data is not None:
        response['data'] = data
    return jsonify(response), code


# 为了向后兼容，保留旧的函数名（可选）
def success_response(data: Any = None, message: str = 'success', status_code: int = 200) -> tuple:
    """向后兼容的成功响应函数"""
    return success(data=data, msg=message)


def error_response(message: str = '操作失败', status_code: int = 400, errors: Optional[Dict] = None) -> tuple:
    """向后兼容的错误响应函数"""
    return fail(code=status_code, msg=message, data=errors)

