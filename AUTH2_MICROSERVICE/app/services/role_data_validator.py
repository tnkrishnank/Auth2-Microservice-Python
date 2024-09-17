from .db_get_queries import *

def check_role_exists(role):
    role_count = get_role_count(role)
    if role_count == 0:
        raise Exception("Role does not exist.")
    return True

def check_role_enabled(role):
    role = get_role(role)
    if role:
        return role.enabled
    return False