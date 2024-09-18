from .db_get_queries import *

def check_role_exists(role):
    role_count = get_role_count(role)
    if role_count == 0:
        raise Exception("Role does not exist.")
    return True

def check_role_not_exists(role):
    role_count = get_role_count(role)
    if role_count > 0:
        raise Exception("Role already exists.")
    return True

def check_role_enabled(role):
    role = get_role(role)
    if role:
        return role.enabled
    return False

def check_permission_on_role(role, permission):
    permission_on_role = get_permission_on_role(role, permission)
    if not permission_on_role:
        raise Exception("Permission on role does not exist.")
    return True

def check_permission_not_on_role(role, permission):
    permission_on_role = get_permission_on_role(role, permission)
    if permission_on_role:
        raise Exception("Permission on role already exists.")
    return True