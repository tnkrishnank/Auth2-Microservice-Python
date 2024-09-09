from app import api, db
from app.services import *
from app.utils import fill_authentication_schema

from flask import request
from flask_restx import Namespace, Resource
from datetime import datetime

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
            return "Empty Request Data.", 403
        try:
            validate_username(data['username'])
            check_username_exists(data['username'])
            verify_user(data['username'], data['password'])
            new_auth = Authentications(
                user_id=get_user(data['username']).id,
                auth_token=generate_auth_token(),
                creation_dt=datetime.utcnow(),
                duration=data['duration'] if data['duration'] else 3600
            )
            db.session.add(new_auth)
            db.session.commit()
            auth_data = fill_authentication_schema(data['username'], new_auth.auth_token)
            return auth_data, 201
        except Exception as e:
            return str(e), 403