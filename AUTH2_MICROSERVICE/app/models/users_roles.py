from app import db

class UsersRoles(db.Model):
    __tablename__ = 'users_roles'

    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.BigInteger, db.ForeignKey('roles.id'), primary_key=True)