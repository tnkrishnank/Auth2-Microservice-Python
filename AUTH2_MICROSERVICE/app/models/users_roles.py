from app import db

class UsersRoles(db.Model):
    __tablename__ = 'users_roles'

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.BigInteger, db.ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)