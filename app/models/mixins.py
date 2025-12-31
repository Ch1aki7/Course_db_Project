"""
模型混入类 (Mixins)
提供通用的模型功能
"""
from datetime import datetime
from typing import Dict, Any


class ToDictMixin:
    """序列化混入类，将模型转换为字典"""
    
    def to_dict(self, exclude: list = None) -> Dict[str, Any]:
        """
        将模型实例转换为字典
        
        Args:
            exclude: 要排除的字段列表
        
        Returns:
            模型字段的字典表示
        """
        if exclude is None:
            exclude = []
        
        result = {}
        for column in self.__table__.columns:
            if column.name in exclude:
                continue
            
            value = getattr(self, column.name)
            # 处理 datetime 对象
            if isinstance(value, datetime):
                value = value.isoformat()
            result[column.name] = value
        
        return result

