from app import api
from app.services import *
from app.utils import fill_authentication_schema

from flask import request
from flask_restx import Namespace, Resource

login_request_schema = api.models['LoginRequestSchema']
authentication_schema = api.models['AuthenticationSchema']

api = Namespace('login-controller', description='Login Controller')

@api.route("/authenticate")
class Login(Resource):
    @api.doc(description='Authenticate User Account')
    @api.response(201, 'Created', authentication_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(login_request_schema, validate=True)
    def post(self):
        data = request.json
        if login_request_schema is None:
            return {"msg": "Empty Request Data."}, 403
        try:
            validate_username(data['username'])
            check_username_exists(data['username'])
            check_user_enabled(data['username'])
            verify_user(data['username'], data['password'])
            new_auth = create_authentication(data['username'], data['duration'])
            update_user_login_dt(data['username'])
            auth_data = fill_authentication_schema(data['username'], new_auth.auth_token)
            return auth_data, 201
        except Exception as e:
            return {"msg": str(e)}, 403