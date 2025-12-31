"""
工具类模块
包含统一响应、异常处理、Schema 基类等通用功能
"""
from app.utils.response import success, fail
from app.utils.exceptions import (
    APIException, ValidationError, NotFoundError,
    UnauthorizedError, ForbiddenError, register_error_handlers
)
from app.utils.schemas import (
    BaseSchema, BaseQuerySchema, BaseCreateSchema,
    BaseUpdateSchema, PaginationSchema, IDSchema
)

__all__ = [
    # 响应函数
    'success', 'fail',
    # 异常类
    'APIException', 'ValidationError', 'NotFoundError',
    'UnauthorizedError', 'ForbiddenError', 'register_error_handlers',
    # Schema 基类
    'BaseSchema', 'BaseQuerySchema', 'BaseCreateSchema',
    'BaseUpdateSchema', 'PaginationSchema', 'IDSchema'
]

