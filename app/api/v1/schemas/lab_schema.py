"""
实验室 Schema 定义
用于数据验证和序列化
"""
from marshmallow import fields, validate
from app.utils.schemas import BaseCreateSchema, BaseUpdateSchema, BaseSchema


class LaboratorySchema(BaseSchema):
    """实验室 Schema（用于响应）"""
    id = fields.Integer(dump_only=True, description='实验室ID')
    name = fields.String(required=True, validate=validate.Length(min=1, max=50), description='实验室名称')
    location = fields.String(allow_none=True, validate=validate.Length(max=100), description='实验室位置')


class LaboratoryCreateSchema(BaseCreateSchema):
    """创建实验室 Schema（用于 POST 请求）"""
    name = fields.String(required=True, validate=validate.Length(min=1, max=50), error_messages={
        'required': '实验室名称不能为空',
        'invalid': '实验室名称格式错误'
    }, description='实验室名称')
    location = fields.String(allow_none=True, validate=validate.Length(max=100), error_messages={
        'invalid': '实验室位置长度不能超过100个字符'
    }, description='实验室位置')


class LaboratoryUpdateSchema(BaseUpdateSchema):
    """更新实验室 Schema（用于 PUT 请求）"""
    name = fields.String(validate=validate.Length(min=1, max=50), error_messages={
        'invalid': '实验室名称格式错误'
    }, description='实验室名称')
    location = fields.String(allow_none=True, validate=validate.Length(max=100), error_messages={
        'invalid': '实验室位置长度不能超过100个字符'
    }, description='实验室位置')

