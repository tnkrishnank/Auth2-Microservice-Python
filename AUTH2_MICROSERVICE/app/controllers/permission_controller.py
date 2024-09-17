from app import api
from app.services import *

from flask import request
from flask_restx import Namespace, Resource

api = Namespace('permission-controller', description='Permission Controller')