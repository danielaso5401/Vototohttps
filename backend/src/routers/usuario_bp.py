from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import time
# import schemas
from flask import Blueprint

from controllers.usuarioController import create_usuario, usuarios

usuario_bp = Blueprint('roles_bp', __name__)

usuario_bp.route('/create_usuario', methods=['POST'])(create_usuario)
usuario_bp.route('/get_usuario', methods=['GET'])(usuarios)
