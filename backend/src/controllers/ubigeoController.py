from flask import render_template, redirect, url_for, request, abort
from models.Ubigeo import Ubigeo
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# cors = CORS(app)

def create_ubigeo():
    print(request.json)
    ubigeo_departamento=request.json["ubigeo_departamento"]

    new_ubigeo = Ubigeo(ubigeo_departamento)

    db.session.add(new_ubigeo)
    db.session.commit()

    return ubigeo_schema.jsonify(new_ubigeo)

def ubigeos():
    all_ubigeos = Ubigeo.query.all()
    result = ubigeo_schemas.dump(all_ubigeos)
    return jsonify(result)