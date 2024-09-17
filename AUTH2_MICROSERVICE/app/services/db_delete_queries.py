from app import db
from app.models import *
from .db_get_queries import *

# USER RELATED QUERIES
def delete_user(username):
    user = get_user(username)
    if not user:
        raise Exception('User not found.')
    db.session.delete(user)
    db.session.commit()
    return True

def delete_user_permission(username, permission):
    user = get_user(username)
    if not user:
        raise Exception('User not found.')
    permission = get_permission(permission)
    if not permission:
        raise Exception('Permission not found.')
    user_permission = UsersPermissions.query.filter_by(user_id=user.id,permission_id=permission.id).first()
    if not user_permission:
        raise Exception('Permission User mapping not found.')
    db.session.delete(user_permission)
    db.session.commit()
    return True

def delete_user_permissions(username):
    user = get_user(username)
    if not user:
        raise Exception('User not found.')
    UsersPermissions.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return True

def delete_user_role(username, role):
    user = get_user(username)
    if not user:
        raise Exception('User not found.')
    role = get_role(role)
    if not role:
        raise Exception('Role not found.')
    user_role = UsersRoles.query.filter_by(user_id=user.id,role_id=role.id).first()
    if not user_role:
        raise Exception('Role User mapping not found.')
    db.session.delete(user_role)
    db.session.commit()
    return True

def delete_user_roles(username):
    user = get_user(username)
    if not user:
        raise Exception('User not found.')
    UsersRoles.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    return True