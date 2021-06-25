from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import Blueprint
import time
# import schemas
from controllers.electorController import create_elector, electores, elector

elector_bp = Blueprint('elector_bp', __name__)

elector_bp.route('/create_elector', methods=['POST'])(create_elector)
elector_bp.route('/get_elector', methods=['GET'])(electores)
elector_bp.route('/get_elector/<int:id>', methods=['GET'])(elector)
