from flask import render_template, redirect, url_for, request, abort
from models.Roles import Roles
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

db = SQLAlchemy()
# cors = CORS(app)

@cross_origin()
def create_roles():
    print(request.json)

    roles_descripcion = request.json['roles_descripcion']
    new_rol = Roles(roles_descripcion)
    db.session.add(new_rol)
    db.session.commit()

    return roles_schema.jsonify(new_rol)

@cross_origin()
def roles():
    all_roles = Roles.query.all()
    result = roles_schemas.dump(all_roles)
    return jsonify(result)