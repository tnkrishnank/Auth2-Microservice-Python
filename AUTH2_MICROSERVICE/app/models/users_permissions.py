from app import db

class UsersPermissions(db.Model):
    __tablename__ = 'users_permissions'

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    permission_id = db.Column(db.BigInteger, db.ForeignKey('permissions.id', ondelete='CASCADE'), primary_key=True)