from app import db
from app.models import *

from sqlalchemy import func

def get_user_roles(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
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
    if not user:
        raise Exception('User not found.')
    permissions = db.session.query(Permissions.permission).join(UsersPermissions).filter(UsersPermissions.user_id==user.id).all()
    return [permission[0] for permission in permissions]

def get_permission_id(permission):
    permission = Permissions.query.filter_by(permission=permission).first()
    return permission.id if permission else None

def get_permission_count(permission):
    count = db.session.query(func.count(Permissions.permission)).filter_by(permission=permission).scalar()
    return count

def get_all_usernames():
    usernames = db.session.query(Users.username).all()
    return usernames

def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return user

def get_user_contact(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    contact = Contacts.query.filter_by(user_id=user.id).first()
    return contact

def get_user_address(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
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

def delete_user(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    db.session.delete(user)
    db.session.commit()
    return True

def delete_user_permissions(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    UsersPermissions.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return True

def delete_user_permission(username, permission):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    permission_obj = Permissions.query.filter_by(permission=permission).first()
    if not permission_obj:
        raise Exception('Permission not found.')
    user_permission = UsersPermissions.query.filter_by(user_id=user.id, permission_id=permission_obj.id).first()
    if not user_permission:
        raise Exception('Permission User mapping not found.')
    db.session.delete(user_permission)
    db.session.commit()
    return True

def delete_user_roles(username):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    UsersRoles.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return True

def delete_user_role(username, role):
    user = Users.query.filter_by(username=username).first()
    if not user:
        raise Exception('User not found.')
    role_obj = Roles.query.filter_by(role=role).first()
    if not role_obj:
        raise Exception('Role not found.')
    user_role = UsersRoles.query.filter_by(user_id=user.id, role_id=role_obj.id).first()
    if not user_role:
        raise Exception('Role User mapping not found.')
    db.session.delete(user_role)
    db.session.commit()
    return True