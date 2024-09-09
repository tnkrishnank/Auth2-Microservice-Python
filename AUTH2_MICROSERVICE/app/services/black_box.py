from app import db
from app.models import Permissions, Roles

from .db_queries import *

import secrets
import hashlib

def check_permission_exists(permission):
    permission_count = get_permission_count(permission)
    if permission_count == 0:
        raise Exception("Permission does not exist.")
    return True

def check_role_exists(role):
    role_count = get_role_count(role)
    if role_count == 0:
        raise Exception("Role does not exist.")
    return True

def verify_user(username, password):
    password_hash = get_password_hash(password)
    user = get_user(username)
    if not user:
        raise Exception("User Not Found.")
    if password_hash != user.password:
        raise Exception("Invalid Password.")
    return True

def generate_auth_token():
    return secrets.token_hex(32)

def get_password_hash(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    hex_digest = hash_object.hexdigest()
    return hex_digest