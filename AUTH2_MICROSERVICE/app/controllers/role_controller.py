from app import api
from app.services import *

from flask import request
from flask_restx import Namespace, Resource

api = Namespace('role-controller', description='Role Controller')