from app import db

class PermissionsRoles(db.Model):
    __tablename__ = 'permissions_roles'

    permission_id = db.Column(db.BigInteger, db.ForeignKey('permissions.id'), primary_key=True)
    role_id = db.Column(db.BigInteger, db.ForeignKey('roles.id'), primary_key=True)