from app import db

class Contacts(db.Model):
    __tablename__ = 'contacts'

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    skype = db.Column(db.String(255), nullable=True)
    facebook = db.Column(db.String(255), nullable=True)
    linkedin = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    note = db.Column(db.String(255), nullable=True)