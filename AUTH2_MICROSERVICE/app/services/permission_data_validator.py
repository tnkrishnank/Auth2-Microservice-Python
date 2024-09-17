from .db_get_queries import *

def check_permission_exists(permission):
    permission_count = get_permission_count(permission)
    if permission_count == 0:
        raise Exception("Permission does not exist.")
    return True