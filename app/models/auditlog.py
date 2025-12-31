"""
审计日志模型
"""
from datetime import datetime
from app import db
from app.models.mixins import ToDictMixin


class AuditLog(db.Model, ToDictMixin):
    """审计日志表"""
    __tablename__ = 'auditlog'
    
    id = db.Column(db.BigInteger, primary_key=True, comment='日志ID')
    operator_id = db.Column(db.String(20), nullable=False, comment='操作人ID')
    action_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, comment='操作时间')
    action_type = db.Column(db.String(20), nullable=False, comment='操作类型')
    detail = db.Column(db.Text, nullable=True, comment='操作详情')
    ip_address = db.Column(db.String(45), nullable=True, comment='IP地址')
    
    def __repr__(self):
        return f'<AuditLog {self.id}: {self.operator_id} - {self.action_type}>'

