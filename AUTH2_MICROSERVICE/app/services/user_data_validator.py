from .db_get_queries import *

import re
import hashlib

def validate_username(username):
    pattern = r'^[a-z0-9]{5,}$'
    regex = re.compile(pattern)
    if len(username) < 5:
        raise Exception("Username lenght must be between 5 and 128.")
    if not regex.match(username):
        raise Exception("Username can only contain aplphanumeric characters.")
    return True

def validate_password(password):
    pattern = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,20}$'
    regex = re.compile(pattern)
    if len(password) < 8 or len(password) > 20:
        raise Exception("Password must be between 8 and 20 characters long.")
    if not regex.match(password):
        raise Exception("Password must contain at least one digit, one uppercase letter, one lowercase letter, one special character and no whitespaces.")
    return True

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    regex = re.compile(pattern)
    if len(email) > 256:
        raise Exception("Email is too long: Maximum number of characters is 256.")
    elif not regex.match(email):
        raise Exception("Invalid email format.")
    return True

def validate_phone(phone):
    if phone:
        pattern = r'^(\+91)?\d{10}$'
        regex = re.compile(pattern)
        if not regex.match(phone):
            raise Exception("Invalid phone format.")
    return True

def check_username_exists(username):
    username_count = get_username_count(username)
    if username_count == 0:
        raise Exception("Username does not exist.")
    return True

def check_username_not_exists(username):
    username_count = get_username_count(username)
    if username_count > 0:
        raise Exception("Username already exists.")
    return True

def check_email_exists(email):
    email_count = get_email_count(email)
    if email_count == 0:
        raise Exception("Email does not exist.")
    return True

def check_email_not_exists(email):
    email_count = get_email_count(email)
    if email_count > 0:
        raise Exception("Email already exists.")
    return True

def check_phone_exists(phone):
    phone_count = get_phone_count(phone)
    if phone_count == 0:
        raise Exception("Phone does not exist.")
    return True

def check_phone_not_exists(phone):
    phone_count = get_phone_count(phone)
    if phone_count > 0:
        raise Exception("Phone already exists.")
    return True

def strip_phone(phone):
    if phone[0] == '+':
        return phone[3:]
    return phone

def check_secured_user(username):
    user = get_user(username)
    if not user.secured:
        raise Exception("Not a secured user.")
    return True

def check_not_secured_user(username):
    user = get_user(username)
    if user.secured:
        raise Exception("It is a secured user.")
    return True

def check_user_enabled(username):
    user = get_user(username)
    if not user.enabled:
        raise Exception("User not enabled.")
    return True

def check_user_not_enabled(username):
    user = get_user(username)
    if user.enabled:
        raise Exception("User enabled.")
    return True

def check_permission_on_user(username, permission):
    permission_on_user = get_permission_on_user(username, permission)
    if not permission_on_user:
        raise Exception("Permission on user does not exist.")
    return True

def check_permission_not_on_user(username, permission):
    permission_on_user = get_permission_on_user(username, permission)
    if permission_on_user:
        raise Exception("Permission on user already exists.")
    return True

def check_role_on_user(username, role):
    role_on_user = get_role_on_user(username, role)
    if not role_on_user:
        raise Exception("Role on user does not exist.")
    return True

def check_role_not_on_user(username, role):
    role_on_user = get_role_on_user(username, role)
    if role_on_user:
        raise Exception("Role on user already exists.")
    return True