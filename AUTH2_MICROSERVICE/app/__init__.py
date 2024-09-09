from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.DevelopmentConfig')
    app.config.from_object('app.config.MySQLConfig')

    api.init_app(app, title = 'AUTH2 MICROSERVICE', version = '1.0')
    db.init_app(app)

    from app.utils import generate_custom_schemas
    generate_custom_schemas()

    with app.app_context():
        from app.controllers import login_controller, permission_controller, role_controller, user_controller

        api.add_namespace(login_controller.api, path='/login')
        api.add_namespace(permission_controller.api, path='/permission')
        api.add_namespace(role_controller.api, path='/role')
        api.add_namespace(user_controller.api, path='/user')

        db.create_all()

    return app