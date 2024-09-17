from .db_get_queries import *

def check_role_exists(role):
    role_count = get_role_count(role)
    if role_count == 0:
        raise Exception("Role does not exist.")
    return True