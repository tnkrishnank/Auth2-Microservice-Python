from app import db
from app.models import *

from sqlalchemy import func

# USER RELATED QUERIES
def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return user

def get_user_contact(username):
    user = get_user(username)
    if user:
        contact = Contacts.query.filter_by(user_id=user.id).first()
        return contact
    return None

def get_user_address(username):
    user = get_user(username)
    if user:
        address = Addresses.query.filter_by(user_id=user.id).first()
        return address
    return None

def get_all_usernames():
    usernames = db.session.query(Users.username).all()
    return [username[0] for username in usernames] if usernames else None

def get_username_count(username):
    count = db.session.query(func.count(Users.username)).filter_by(username=username).scalar()
    return count

def get_email_count(email):
    count = db.session.query(func.count(Contacts.email)).filter_by(email=email).scalar()
    return count

def get_phone_count(phone):
    count = db.session.query(func.count(Contacts.phone)).filter_by(phone=phone).scalar()
    return count

def get_user_permissions(username):
    user = get_user(username)
    if user:
        permissions = db.session.query(Permissions.permission).join(UsersPermissions).filter(UsersPermissions.user_id==user.id).all()
        return [permission[0] for permission in permissions] if permissions else None
    return None

def get_user_permission_count(username):
    user = get_user(username)
    if user:
        permission_count = UsersPermissions.query.filter_by(user_id=user.id).count()
        return permission_count
    return 0

def get_user_roles(username):
    user = get_user(username)
    if user:
        roles = db.session.query(Roles.role).join(UsersRoles).filter(UsersRoles.user_id==user.id).all()
        return [role[0] for role in roles] if roles else None
    return None

def get_user_role_count(username):
    user = get_user(username)
    if user:
        role_count = UsersRoles.query.filter_by(user_id=user.id).count()
        return role_count
    return 0

def get_permission_on_user(username, permission):
    permission = get_permission(permission)
    user = get_user(username)
    permission_user = UsersPermissions.query.filter_by(permission_id=permission.id, user_id=user.id).first()
    return permission_user if permission_user else None

def get_role_on_user(username, role):
    role = get_role(role)
    user = get_user(username)
    role_user = UsersRoles.query.filter_by(role_id=role.id, user_id=user.id).first()
    return role_user if role_user else None

# PERMISSION RELATED QUERIES
def get_permission(permission):
    permission = Permissions.query.filter_by(permission=permission).first()
    return permission

def get_permission_id(permission):
    permission = get_permission(permission)
    return permission.id if permission else None

def get_permission_count(permission):
    count = db.session.query(func.count(Permissions.permission)).filter_by(permission=permission).scalar()
    return count

def get_all_permissions():
    permissions = db.session.query(Permissions.permission).all()
    return [permission[0] for permission in permissions] if permissions else None

def get_permissions_by_role(role):
    role = get_role(role)
    if role:
        permissions = db.session.query(Permissions.permission).join(PermissionsRoles).filter(PermissionsRoles.role_id==role.id).all()
        return [permission[0] for permission in permissions] if permissions else None
    return None

# ROLE RELATED QUERIES
def get_role(role):
    role = Roles.query.filter_by(role=role).first()
    return role

def get_role_id(role):
    role = get_role(role)
    return role.id if role else None

def get_role_count(role):
    count = db.session.query(func.count(Roles.role)).filter_by(role=role).scalar()
    return count

def get_all_roles():
    roles = db.session.query(Roles.role).all()
    return [role[0] for role in roles] if roles else None

def get_permission_on_role(role, permission):
    role = Roles.query.filter_by(role=role).first()
    permission = Permissions.query.filter_by(permission=permission).first()
    permission_role = PermissionsRoles.query.filter_by(role_id=role.id, permission_id=permission.id).first()
    return permission_role if permission_role else None

# AUTHENTICATION RELATED QUERIES
def get_auth(auth_token):
    auth = Authentications.query.filter_by(auth_token=auth_token).first()
    return auth

def get_user_by_auth_token(auth_token):
    auth = get_auth(auth_token)
    if auth:
        user = Users.query.filter_by(id=auth.user_id).first()
        return user
    return None