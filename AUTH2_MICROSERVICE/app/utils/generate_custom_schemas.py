from app import api
from app.models import *
from .sqlalchemy_to_restx_model import sqlalchemy_to_restx_model_exclude, sqlalchemy_to_restx_model_include

from flask_restx import fields

def generate_custom_schemas():
    sqlalchemy_to_restx_model_exclude(Addresses, 'AddressSchema', exclude_columns=['user_id'])
    sqlalchemy_to_restx_model_exclude(Contacts, 'ContactSchema', exclude_columns=['user_id'])
    additional_fields = {
        'contact': fields.Nested(api.models['ContactSchema']),
        'address': fields.Nested(api.models['AddressSchema']),
        'roles': fields.List(fields.String),
        'permissions': fields.List(fields.String)
    }
    sqlalchemy_to_restx_model_exclude(Users, 'UserSchema', exclude_columns=['id', 'password'], additional_fields=additional_fields)

    sqlalchemy_to_restx_model_exclude(Users, 'CreateUpdateUserSchema', exclude_columns=['id', 'creation_dt', 'updated_dt', 'login_dt'], additional_fields=additional_fields)

    column = Authentications.__table__.columns['duration']
    additional_fields = {
        'duration': fields.String(required=not column.nullable, default=column.default.arg if column.default is not None else None)
    }
    sqlalchemy_to_restx_model_include(Users, 'LoginRequestSchema', include_columns=['username', 'password'], additional_fields=additional_fields)

    column = Users.__table__.columns['username']
    additional_fields = {
        'username': fields.String(required=not column.nullable, default=column.default.arg if column.default is not None else None)
    }
    sqlalchemy_to_restx_model_exclude(Authentications, 'AuthenticationSchema', exclude_columns=['user_id'], additional_fields=additional_fields)