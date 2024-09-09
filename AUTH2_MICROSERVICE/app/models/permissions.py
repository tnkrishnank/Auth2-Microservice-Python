from app import db

class Permissions(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    permission = db.Column(db.String(80), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    resource_path = db.Column(db.String(1023), nullable=True)
    access_type = db.Column(db.String(255), nullable=True)
    note = db.Column(db.String(255), nullable=True)