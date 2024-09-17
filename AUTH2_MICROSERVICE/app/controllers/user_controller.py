from app import api
from app.services import *
from app.utils import fill_user_schema

from flask import request
from flask_restx import Namespace, Resource

create_update_user_schema = api.models['CreateUpdateUserSchema']
user_schema = api.models['UserSchema']

api = Namespace('user-controller', description='User Controller')

@api.route("/<string:auth_token>/create")
class CreateUser(Resource):
    @api.doc(description='Create User Account')
    @api.response(201, 'Created', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(create_update_user_schema, validate=True)
    @check_permissions(['CREATE_USER'])
    def post(self):
        data = request.json
        if create_update_user_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            validate_username(data['username'])
            check_username_not_exists(data['username'])
            validate_password(data['password'])
            validate_email(data['contact']['email'])
            check_email_not_exists(data['contact']['email'])
            validate_phone(data['contact']['phone'])
            check_phone_not_exists(data['contact']['phone'])
            data['contact']['phone'] = strip_phone(data['contact']['phone'])
            for i in data['permissions']:
                check_permission_exists(i)
            for i in data['roles']:
                check_role_exists(i)
            create_user(data)
            create_contact(data['username'], data['contact'])
            create_address(data['username'], data['address'])
            for i in data['permissions']:
                create_user_permission(data['username'], i)
            for i in data['roles']:
                create_user_role(data['username'], i)
            user_data = fill_user_schema(data['username'])
            return user_data, 201
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:username>")
class RUDUser(Resource):
    @api.doc(description='Get User Account')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['READ_USER'])
    def get(self, username):
        try:
            check_username_exists(username)
            user_data = fill_user_schema(username)
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Update User Account')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(create_update_user_schema, validate=True)
    @check_permissions(['UPDATE_USER'])
    def put(self, username):
        data = request.json
        if create_update_user_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            user = get_user(username)
            contact = get_user_contact(username)
            address = get_user_address(username)
            check_username_exists(user.username)
            if user.username != data['username']:
                check_username_not_exists(data['username'])
            if user.password != get_password_hash(data['password']):
                validate_password(data['password'])
            if contact.email != data['contact']['email']:
                validate_email(data['contact']['email'])
                check_email_not_exists(data['contact']['email'])
            validate_phone(data['contact']['phone'])
            data['contact']['phone'] = strip_phone(data['contact']['phone'])
            if contact.phone != data['contact']['phone']:
                check_phone_not_exists(data['contact']['phone'])
            for i in data['permissions']:
                check_permission_exists(i)
            for i in data['roles']:
                check_role_exists(i)
            update_user(data['username'], data)
            update_contact(data['username'], data['contact'])
            update_address(data['username'], data['address'])
            delete_user_permissions(username)
            for i in data['permissions']:
                create_user_permission(data['username'], i)
            delete_user_roles(username)
            for i in data['roles']:
                create_user_role(data['username'], i)
            user_data = fill_user_schema(data['username'])
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete User Account')
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_USER'])
    def delete(self, username):
        try:
            check_username_exists(username)
            check_not_secured_user(username)
            delete_user(username)
            return {"msg": "User Deleted."}, 200
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:username>/roles/<string:role>")
class UserRole(Resource):
    @api.doc(description='Add role on a user')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['ADD_ROLE_USER'])
    def post(self, username, role):
        try:
            check_username_exists(username)
            check_role_exists(role)
            create_user_role(username, role)
            user_data = fill_user_schema(username)
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete role on a user')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_ROLE_USER'])
    def delete(self, username, role):
        try:
            delete_user_role(username, role)
            user_data = fill_user_schema(username)
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

@api.route("/<string:auth_token>/<string:username>/permissions/<string:permission>")
class UserPermission(Resource):
    @api.doc(description='Add permission on a user')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['ADD_PERMISSION_USER'])
    def post(self, username, permission):
        try:
            check_username_exists(username)
            check_permission_exists(permission)
            create_user_permission(username, permission)
            user_data = fill_user_schema(username)
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403

    @api.doc(description='Delete permission on a user')
    @api.response(200, 'Success', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @check_permissions(['DELETE_PERMISSION_USER'])
    def delete(self, username, permission):
        try:
            delete_user_permission(username, permission)
            user_data = fill_user_schema(username)
            return user_data, 200
        except Exception as e:
            return {"msg": str(e)}, 403