"""
实验室模型
"""
from app import db
from app.models.mixins import ToDictMixin


class Laboratory(db.Model, ToDictMixin):
    """实验室表"""
    __tablename__ = 'laboratory'
    
    id = db.Column(db.Integer, primary_key=True, comment='实验室ID')
    name = db.Column(db.String(50), nullable=False, comment='实验室名称')
    location = db.Column(db.String(100), nullable=True, comment='实验室位置')
    
    # 关系定义
    teachers = db.relationship('Teacher', backref='laboratory', lazy='dynamic')
    students = db.relationship('Student', backref='laboratory', lazy='dynamic')
    equipment = db.relationship('Equipment', backref='laboratory', lazy='dynamic')
    admins = db.relationship('Admin', backref='laboratory', lazy='dynamic')
    
    def __repr__(self):
        return f'<Laboratory {self.id}: {self.name}>'

