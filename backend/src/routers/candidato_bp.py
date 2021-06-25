from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import Blueprint
import time
# import models.schemas
from controllers.candidatoController import create_candidato, candidatos
# from controllers import candidatoController

candidato_bp = Blueprint('candidato_bp', __name__)

candidato_bp.route('/create_candidato', methods=['POST'])(create_candidato)
candidato_bp.route('/get_candidato', methods=['GET'])(candidatos)
