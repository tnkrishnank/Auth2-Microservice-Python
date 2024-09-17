from app import db
from app.models import *
from app.utils.time import get_current_datetime
from .db_get_queries import *

import secrets
import hashlib
from datetime import timedelta

def check_permissions(required_permission):
    def decorator(f):
        def decorated_function(*args, **kwargs):
            if 'auth_token' in kwargs:
                try:
                    validate_access(required_permission[0], kwargs.get('auth_token'))
                    kwargs.pop('auth_token')
                    return f(*args, **kwargs)
                except Exception as e:
                    return {"msg": str(e)}, 401
            return {"msg": "Unauthorized"}, 401
        return decorated_function
    return decorator

def validate_access(permission, auth_token):
    validate_auth_token(auth_token)
    user = get_user_by_auth_token(auth_token)
    if get_user_role_count(user.username) == 0 and get_user_permission_count(user.username) == 0:
        raise Exception("No role or permission defined for the user.")
    roles = get_user_roles(user.username)
    permissions = get_user_permissions(user.username)
    if permissions is None:
        permissions = []
    if roles is not None:
        for role in roles:
            perms = get_permissions_by_role(role)
            for perm in perms:
                if perm not in permissions:
                    permissions.append(perm)
    for perm in permissions:
        if perm == permission:
            return True
    raise Exception("Unauthorized")

def validate_auth_token(auth_token):
    auth = get_auth(auth_token)
    if not auth:
        raise Exception('Invalid auth token.')
    expiration_time = auth.creation_dt + timedelta(seconds=auth.duration)
    if not get_current_datetime() < expiration_time:
        raise Exception('Auth token expired.')
    return True

def generate_auth_token():
    return secrets.token_hex(32)

def verify_user(username, password):
    password_hash = get_password_hash(password)
    user = get_user(username)
    if not user:
        raise Exception("User Not Found.")
    if password_hash != user.password:
        raise Exception("Invalid Password.")
    return True

def get_password_hash(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    hex_digest = hash_object.hexdigest()
    return hex_digest