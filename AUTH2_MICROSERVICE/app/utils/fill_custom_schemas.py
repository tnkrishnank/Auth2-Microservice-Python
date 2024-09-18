from app import api
from app.services.db_get_queries import *

from flask_restx import marshal

def fill_user_schema(username):
    address_schema = api.models['AddressSchema']
    contact_schema = api.models['ContactSchema']
    user_schema = api.models['UserSchema']
    user = get_user(username)
    contact = get_user_contact(username)
    address = get_user_address(username)
    user_data = marshal(user, user_schema)
    user_data['contact'] = marshal(contact, contact_schema)
    user_data['address'] = marshal(address, address_schema)
    user_data['roles'] = get_user_roles(username)
    user_data['permissions'] = get_user_permissions(username)
    return user_data

def fill_permission_schema(permission):
    permission_schema = api.models['PermissionSchema']
    permission = get_permission(permission)
    permission_data = marshal(permission, permission_schema)
    return permission_data

def fill_role_schema(role):
    role_schema = api.models['RoleSchema']
    role = get_role(role)
    role_data = marshal(role, role_schema)
    return role_data

def fill_full_role_schema(role):
    full_role_schema = api.models['FullRoleSchema']
    role = get_role(role)
    role_data = marshal(role, full_role_schema)
    role_data['permissions'] = get_permissions_by_role(role.role)
    return role_data

def fill_authentication_schema(username, auth_token):
    authentication_schema = api.models['AuthenticationSchema']
    auth = get_auth(auth_token)
    auth_data = marshal(auth, authentication_schema)
    auth_data['username'] = username
    return auth_data