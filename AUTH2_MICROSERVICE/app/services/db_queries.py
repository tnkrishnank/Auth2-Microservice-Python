from app import db
from app.models import *

from sqlalchemy import func

def get_user_roles(username):
    user = Users.query.filter_by(username=username).first()
    roles = db.session.query(Roles.role).join(UsersRoles).filter(UsersRoles.user_id==user.id).all()
    return [role[0] for role in roles]

def get_role_id(role):
    role = Roles.query.filter_by(role=role).first()
    return role.id if role else None

def get_role_count(role):
    count = db.session.query(func.count(Roles.role)).filter_by(role=role).scalar()
    return count

def get_user_permissions(username):
    user = Users.query.filter_by(username=username).first()
    permissions = db.session.query(Permissions.permission).join(UsersPermissions).filter(UsersPermissions.user_id==user.id).all()
    return [permission[0] for permission in permissions]

def get_permission_id(permission):
    permission = Permissions.query.filter_by(permission=permission).first()
    return permission.id if permission else None

def get_permission_count(permission):
    count = db.session.query(func.count(Permissions.permission)).filter_by(permission=permission).scalar()
    return count

def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return user

def get_user_contact(username):
    user = Users.query.filter_by(username=username).first()
    contact = Contacts.query.filter_by(user_id=user.id).first()
    return contact

def get_user_address(username):
    user = Users.query.filter_by(username=username).first()
    address = Addresses.query.filter_by(user_id=user.id).first()
    return address

def get_username_count(username):
    count = db.session.query(func.count(Users.username)).filter_by(username=username).scalar()
    return count

def get_email_count(email):
    count = db.session.query(func.count(Contacts.email)).filter_by(email=email).scalar()
    return count

def get_phone_count(phone):
    count = db.session.query(func.count(Contacts.phone)).filter_by(phone=phone).scalar()
    return count

def get_auth(username, auth_token):
    auth = db.session.query(Authentications).join(Users).filter(
        Users.username == username,
        Authentications.auth_token == auth_token
        ).first()
    return auth