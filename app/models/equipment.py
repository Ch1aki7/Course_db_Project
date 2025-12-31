"""
设备模型
"""
from app import db
from app.models.mixins import ToDictMixin


class Equipment(db.Model, ToDictMixin):
    """设备表"""
    __tablename__ = 'equipment'
    
    id = db.Column(db.BigInteger, primary_key=True, comment='设备ID')
    name = db.Column(db.String(100), nullable=False, comment='设备名称')
    lab_id = db.Column(db.Integer, db.ForeignKey('laboratory.id'), nullable=True, comment='所属实验室ID')
    category = db.Column(db.Integer, nullable=False, comment='设备类别 (1:学院, 2:实验室)')
    status = db.Column(db.Integer, nullable=False, default=1, comment='设备状态 (1:正常...)')
    
    # 冗余字段
    next_avail_time = db.Column(db.DateTime, nullable=True, comment='下次可用时间（冗余字段）')
    
    # 关系定义
    reservations = db.relationship('Reservation', backref='equipment', lazy='dynamic')
    time_slots = db.relationship('TimeSlot', backref='equipment', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Equipment {self.id}: {self.name}>'

