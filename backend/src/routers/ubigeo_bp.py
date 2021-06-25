from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import time
# import schemas
from flask import Blueprint

from controllers.ubigeoController import create_ubigeo, ubigeos

ubigeo_bp = Blueprint('roles_bp', __name__)

ubigeo_bp.route('/create_ubigeo', methods=['POST'])(create_ubigeo)
ubigeo_bp.route('/get_ubigeo', methods=['GET'])(ubigeos)
