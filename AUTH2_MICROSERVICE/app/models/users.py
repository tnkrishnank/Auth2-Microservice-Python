from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(1), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    creation_dt = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_dt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    login_dt = db.Column(db.DateTime, nullable=True)
    note = db.Column(db.String(255), nullable=True)
    secured = db.Column(db.Boolean, default=False, nullable=False)