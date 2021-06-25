from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import Blueprint

import time
# import schemas
from controllers.loginController import login_post

login_bp = Blueprint('roles_bp', __name__)

login_bp.route('/login', methods=['POST'])(login_post)