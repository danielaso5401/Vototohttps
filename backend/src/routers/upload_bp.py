from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import time
# import schemas
from flask import Blueprint

from controllers.uploadController import upload_file, get_file, upload_file2

upload_bp = Blueprint('upload_bp', __name__)

upload_bp.route('/upload', methods=["GET", "POST"])(upload_file)
upload_bp.route('/uploads/<filename>')(get_file)
upload_bp.route('/upload_reconocedor',  methods=["GET", "POST"])(upload_file2)