from .db_get_queries import *

def check_permission_exists(permission):
    permission_count = get_permission_count(permission)
    if permission_count == 0:
        raise Exception("Permission does not exist.")
    return True

def check_permission_not_exists(permission):
    permission_count = get_permission_count(permission)
    if permission_count > 0:
        raise Exception("Permission already exists.")
    return True

def check_permission_enabled(permission):
    permission = get_permission(permission)
    if permission:
        return permission.enabled
    return False