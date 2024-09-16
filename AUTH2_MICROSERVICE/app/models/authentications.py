from app import db

class Authentications(db.Model):
    __tablename__ = 'authentications'

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    auth_token = db.Column(db.String(255), unique=True, primary_key=True)
    creation_dt = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    duration = db.Column(db.BigInteger, default=3600, nullable=False)