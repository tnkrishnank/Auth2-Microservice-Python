from app import api, db
from app.services import *
from app.models import Users, Addresses, Contacts, UsersPermissions, UsersRoles
from app.utils import fill_user_schema

from flask import request
from flask_restx import Namespace, Resource

create_update_user_schema = api.models['CreateUpdateUserSchema']
user_schema = api.models['UserSchema']

api = Namespace('user-controller', description='User Controller')

@api.route("/create")
class CreateUser(Resource):
    @api.doc(description='Create User Account')
    @api.response(201, 'Created', user_schema)
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.expect(create_update_user_schema, validate=True)
    def post(self):
        data = request.json
        if create_update_user_schema is None:
            return "Empty Request Data.", 403
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
            new_user = Users(
                username=data['username'],
                password=get_password_hash(data['password']),
                name=data['name'],
                surname=data['surname'],
                gender=data['gender'],
                birth_date=data['birth_date'],
                enabled=data['enabled'],
                note=data['note'],
                secured=data['secured']
            )
            db.session.add(new_user)
            db.session.commit()
            new_contact = Contacts(
                user_id=new_user.id,
                email=data['contact']['email'],
                phone=data['contact']['phone'],
                skype=data['contact']['skype'],
                facebook=data['contact']['facebook'],
                linkedin=data['contact']['linkedin'],
                website=data['contact']['website'],
                note=data['contact']['note']
            )
            db.session.add(new_contact)
            db.session.commit()
            new_address = Addresses(
                user_id=new_user.id,
                address=data['address']['address'],
                address2=data['address']['address2'],
                city=data['address']['city'],
                country=data['address']['country'],
                zip_code=data['address']['zip_code']
            )
            db.session.add(new_address)
            db.session.commit()
            for i in data['permissions']:
                new_users_permissions = UsersPermissions(
                    user_id=new_user.id,
                    permission_id=get_permission_id(i)
                )
                db.session.add(new_users_permissions)
                db.session.commit()
            for i in data['roles']:
                new_users_roles = UsersRoles(
                    user_id=new_user.id,
                    role_id=get_role_id(i)
                )
                db.session.add(new_users_roles)
                db.session.commit()
            user_data = fill_user_schema(data['username'])
            return user_data, 201
        except Exception as e:
            return str(e), 403