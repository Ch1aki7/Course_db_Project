"""
Schema 基类
提供 Marshmallow Schema 的基础配置和通用功能
"""
from marshmallow import Schema, EXCLUDE, INCLUDE, RAISE
from marshmallow import fields, validates_schema, ValidationError


class BaseSchema(Schema):
    """
    Schema 基类
    
    配置：
    - 自动过滤 None 值（dump 时）
    - 未知字段处理策略：RAISE（严格模式）
    """
    
    class Meta:
        # 未知字段处理：RAISE（遇到未知字段时抛出异常）
        # 可选值：EXCLUDE（忽略未知字段）、INCLUDE（包含未知字段）、RAISE（抛出异常）
        unknown = RAISE
    
    def dump(self, obj, *, many=None, **kwargs):
        """
        重写 dump 方法，自动过滤 None 值
        
        Args:
            obj: 要序列化的对象
            many: 是否为多个对象
            **kwargs: 其他参数
        
        Returns:
            序列化后的字典，自动过滤 None 值
        """
        result = super().dump(obj, many=many, **kwargs)
        
        # 递归过滤 None 值
        if many:
            return [self._filter_none(data) for data in result]
        else:
            return self._filter_none(result)
    
    @staticmethod
    def _filter_none(data):
        """
        递归过滤字典中的 None 值
        
        Args:
            data: 要过滤的字典
        
        Returns:
            过滤后的字典
        """
        if isinstance(data, dict):
            return {k: BaseSchema._filter_none(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [BaseSchema._filter_none(item) for item in data if item is not None]
        else:
            return data


class BaseQuerySchema(BaseSchema):
    """
    查询参数 Schema 基类
    用于 GET 请求的参数验证
    """
    
    class Meta(BaseSchema.Meta):
        # 查询参数通常更宽松，忽略未知字段
        unknown = EXCLUDE


class BaseCreateSchema(BaseSchema):
    """
    创建数据 Schema 基类
    用于 POST 请求的数据验证
    """
    
    class Meta(BaseSchema.Meta):
        # 创建数据时严格模式，遇到未知字段抛出异常
        unknown = RAISE


class BaseUpdateSchema(BaseSchema):
    """
    更新数据 Schema 基类
    用于 PUT/PATCH 请求的数据验证
    """
    
    class Meta(BaseSchema.Meta):
        # 更新数据时忽略未知字段，允许部分更新
        unknown = EXCLUDE


# 常用字段类型（可选，方便使用）
class PaginationSchema(BaseQuerySchema):
    """分页参数 Schema"""
    page = fields.Integer(missing=1, validate=lambda x: x > 0, error_messages={'invalid': '页码必须为正整数'})
    per_page = fields.Integer(missing=10, validate=lambda x: 0 < x <= 100, error_messages={'invalid': '每页数量必须在1-100之间'})


class IDSchema(BaseQuerySchema):
    """ID 参数 Schema"""
    id = fields.Integer(required=True, validate=lambda x: x > 0, error_messages={'required': 'ID 不能为空', 'invalid': 'ID 必须为正整数'})

