from app import api
from app.services import *
from app.utils import fill_permission_schema

from flask import request
from flask_restx import Namespace, Resource

permission_schema = api.models['PermissionSchema']

api = Namespace('permission-controller', description='Permission Controller')

@api.route("/<string:auth_token>/create")
class CreatePermission(Resource):
    @api.doc(description='Create Permission')
    @api.response(201, 'Created', permission_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(permission_schema, validate=True)
    @check_permissions(['CREATE_PERMISSION'])
    def post(self):
        data = request.json
        if permission_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            check_permission_not_exists(data['permission'])
            create_permission(data)
            permission_data = fill_permission_schema(data['permission'])
            return permission_data, 201
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:permission>")
class RUDPermission(Resource):
    @api.doc(description='Get Permission')
    @api.response(200, 'Success', permission_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['READ_PERMISSION'])
    def get(self, permission):
        try:
            check_permission_exists(permission)
            permission_data = fill_permission_schema(permission)
            return permission_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Update Permission')
    @api.response(200, 'Success', permission_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(permission_schema, validate=True)
    @check_permissions(['UPDATE_PERMISSION'])
    def put(self, permission):
        data = request.json
        if permission_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            check_permission_exists(permission)
            if permission != data['permission']:
                check_permission_not_exists(data['permission'])
            update_permission(permission, data)
            permission_data = fill_permission_schema(data['permission'])
            return permission_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete Permission')
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_PERMISSION'])
    def delete(self, permission):
        try:
            check_permission_exists(permission)
            delete_permission(permission)
            return {"msg": "Permission Deleted."}, 200
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/getallpermissions")
class GetAllPermissions(Resource):
    @api.doc(description='Get All Permissions')
    @api.response(200, 'Success', permission_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['READ_PERMISSION'])
    def get(self):
        try:
            permissions = []
            permissionnames = get_all_permissions()
            for permission in permissionnames:
                permission_data = fill_permission_schema(permission)
                permissions.append(permission_data)
            return permissions, 200
        except Exception as e:
            return {"msg": str(e)}, 403