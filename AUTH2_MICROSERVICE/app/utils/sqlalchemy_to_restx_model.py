from app import api, db

from flask_restx import fields
from datetime import datetime, date

def sqlalchemy_to_restx_model_exclude(model, name, exclude_columns=None, additional_fields=None):
    model_fields = {}
    if exclude_columns is None:
        exclude_columns = []
    for column in model.__table__.columns:
        if column.name in exclude_columns:
            continue
        required = not column.nullable
        default = column.default.arg if column.default is not None else None
        if isinstance(column.type, db.Integer):
            model_fields[column.name] = fields.Integer(required=required, default=default)
        elif isinstance(column.type, db.String):
            model_fields[column.name] = fields.String(required=required, default=default, max_length=column.type.length)
        elif isinstance(column.type, db.Float):
            model_fields[column.name] = fields.Float(required=required, default=default)
        elif isinstance(column.type, db.Boolean):
            model_fields[column.name] = fields.Boolean(required=required, default=default)
        elif isinstance(column.type, db.Date):
            model_fields[column.name] = fields.Date(required=required, default=date.today)
        elif isinstance(column.type, db.DateTime):
            model_fields[column.name] = fields.DateTime(required=required, default=datetime.now)
        elif isinstance(column.type, db.BigInteger):
            model_fields[column.name] = fields.Integer(required=required, default=default)
        elif isinstance(column.type, db.SmallInteger):
            model_fields[column.name] = fields.Integer(required=required, default=default)
    if additional_fields is not None:
        for key in additional_fields.keys():
            model_fields[key] = additional_fields[key]
    return api.model(name, model_fields)

def sqlalchemy_to_restx_model_include(model, name, include_columns=None, additional_fields=None):
    model_fields = {}
    if include_columns is None:
        return api.model(name, model_fields)
    for column in model.__table__.columns:
        if column.name not in include_columns:
            continue
        required = not column.nullable
        default = column.default.arg if column.default is not None else None
        if isinstance(column.type, db.Integer):
            model_fields[column.name] = fields.Integer(required=required, default=default)
        elif isinstance(column.type, db.String):
            model_fields[column.name] = fields.String(required=required, default=default)
        elif isinstance(column.type, db.Float):
            model_fields[column.name] = fields.Float(required=required, default=default)
        elif isinstance(column.type, db.Boolean):
            model_fields[column.name] = fields.Boolean(required=required, default=default)
        elif isinstance(column.type, db.Date):
            model_fields[column.name] = fields.Date(required=required, default=date.today)
        elif isinstance(column.type, db.DateTime):
            model_fields[column.name] = fields.DateTime(required=required, default=datetime.now)
        elif isinstance(column.type, db.BigInteger):
            model_fields[column.name] = fields.Integer(required=required, default=default)
        elif isinstance(column.type, db.SmallInteger):
            model_fields[column.name] = fields.Integer(required=required, default=default)
    if additional_fields is not None:
        for key in additional_fields.keys():
            model_fields[key] = additional_fields[key]
    return api.model(name, model_fields)