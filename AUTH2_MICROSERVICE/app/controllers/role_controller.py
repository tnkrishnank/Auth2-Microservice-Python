from app import api
from app.services import *
from app.utils import fill_full_role_schema

from flask import request
from flask_restx import Namespace, Resource

role_schema = api.models['RoleSchema']
full_role_schema = api.models['FullRoleSchema']

api = Namespace('role-controller', description='Role Controller')

@api.route("/<string:auth_token>/create")
class CreateRole(Resource):
    @api.doc(description='Create Role')
    @api.response(201, 'Created', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(role_schema, validate=True)
    @check_permissions(['CREATE_ROLE'])
    def post(self):
        data = request.json
        if role_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            check_role_not_exists(data['role'])
            create_role(data)
            role_data = fill_full_role_schema(data['role'])
            return role_data, 201
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:role>")
class RUDRole(Resource):
    @api.doc(description='Get Role')
    @api.response(200, 'Success', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['READ_ROLE'])
    def get(self, role):
        try:
            check_role_exists(role)
            role_data = fill_full_role_schema(role)
            return role_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Update Role')
    @api.response(200, 'Success', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(role_schema, validate=True)
    @check_permissions(['UPDATE_ROLE'])
    def put(self, role):
        data = request.json
        if role_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            check_role_exists(role)
            if role != data['role']:
                check_role_not_exists(data['role'])
            update_role(role, data)
            role_data = fill_full_role_schema(data['role'])
            return role_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete Role')
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_ROLE'])
    def delete(self, role):
        try:
            check_role_exists(role)
            delete_role(role)
            return {"msg": "Role Deleted."}, 200
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/getallroles")
class GetAllRoles(Resource):
    @api.doc(description='Get All Roles')
    @api.response(200, 'Success', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['READ_ROLE'])
    def get(self):
        try:
            roles = []
            rolenames = get_all_roles()
            for role in rolenames:
                role_data = fill_full_role_schema(role)
                roles.append(role_data)
            return roles, 200
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:role>/permissions/<string:permission>")
class RolePermission(Resource):
    @api.doc(description='Add permission on a role')
    @api.response(200, 'Success', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['ADD_PERMISSION_ROLE'])
    def post(self, role, permission):
        try:
            check_role_exists(role)
            check_permission_exists(permission)
            check_permission_not_on_role(role, permission)
            create_role_permission(role, permission)
            role_data = fill_full_role_schema(role)
            return role_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete permission on a role')
    @api.response(200, 'Success', full_role_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_PERMISSION_ROLE'])
    def delete(self, role, permission):
        try:
            check_role_exists(role)
            check_permission_exists(permission)
            check_permission_on_role(role, permission)
            delete_role_permission(role, permission)
            role_data = fill_full_role_schema(role)
            return role_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403