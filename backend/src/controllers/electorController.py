from flask import render_template, redirect, url_for, request, abort
from models.Elector import Elector
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def electores():
    all_electores = Elector.query.all()
    result = elector_schemas.dump(all_electores)
    return jsonify(result)

def elector(id):
    post = id
    # all_electores = Elector.query.all()
    # result = elector_schemas.dump(all_electores)
    elector = User.query.get(post)
    result = elector_schemas.dump(elector)
    return jsonify(result)

def create_elector():
    print(request.json)
    elector_name=request.json["elector_name"]
    elector_dni=request.json["elector_dni"]
    elector_image=request.json["elector_image"]
    ubigeo_idUbigeo=request.json['ubigeo_idUbigeo']
    # elector_image = request.files['elector_img'].read()

    new_elector = Elector(elector_name,elector_dni,elector_image,ubigeo_idUbigeo)

    db.session.add(new_elector)
    db.session.commit()

    return elector_schema.jsonify(new_elector)