from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
import logging

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

    access_logger = logging.getLogger('access')
    access_handler = logging.FileHandler('access.log')
    access_formatter = logging.Formatter('%(clientip)s - - [%(asctime)s] "%(method)s %(path)s %(protocol)s" %(status)s %(size)s')
    access_handler.setFormatter(access_formatter)
    access_logger.addHandler(access_handler)
    access_logger.setLevel(logging.INFO)

    @app.before_request
    def log_request_info():
        request.log_info = {
            'clientip': request.remote_addr,
            'method': request.method,
            'path': request.path,
            'protocol': request.environ.get('SERVER_PROTOCOL'),
            'status': '-',
            'size': '-'
        }

    @app.after_request
    def log_response_info(response):
        request.log_info['status'] = response.status_code
        request.log_info['size'] = response.content_length or 0
        access_logger.info('', extra=request.log_info)
        return response

    return app