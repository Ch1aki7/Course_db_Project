"""
数据库模型模块
将所有模型导入此处，便于统一管理

注意：db 对象在 app/__init__.py 中定义
在各模型文件中使用: from app import db
"""
from app import db

# 导入所有模型
from app.models.laboratory import Laboratory
from app.models.teacher import Teacher
from app.models.student import Student
from app.models.equipment import Equipment
from app.models.timeslot import TimeSlot
from app.models.reservation import Reservation
from app.models.admin import Admin
from app.models.auditlog import AuditLog

__all__ = [
    'db',
    'Laboratory',
    'Teacher',
    'Student',
    'Equipment',
    'TimeSlot',
    'Reservation',
    'Admin',
    'AuditLog'
]

