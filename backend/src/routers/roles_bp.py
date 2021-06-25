from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import time
from flask import Blueprint

# import schemas
from controllers.rolesController import create_roles, roles

roles_bp = Blueprint('roles_bp', __name__)

roles_bp.route('/create_roles', methods=['POST'])(create_roles)
roles_bp.route('/get_roles', methods=['GET'])(roles)
