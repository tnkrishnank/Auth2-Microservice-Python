from app import db

class Roles(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    role = db.Column(db.String(80), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    note = db.Column(db.String(255), nullable=True)