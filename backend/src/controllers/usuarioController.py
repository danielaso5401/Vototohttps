from flask import render_template, redirect, url_for, request, abort
from models.Usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# cors = CORS(app)

def create_usuario():
    print(request.json)

    usuario_name=request.json['usuario_name']
    usuario_usuario=request.json['usuario_usuario']
    usuario_contraseña=request.json['usuario_contraseña']
    roles_idRoles=request.json['roles_idRoles']

    new_usuario = Usuario(usuario_name,usuario_usuario,usuario_contraseña,roles_idRoles)

    db.session.add(new_usuario)
    db.session.commit()

    return usuario_schema.jsonify(new_usuario)

def usuarios():
    all_usuarios = Usuario.query.all()
    result = usuario_schemas.dump(all_usuarios)
    return jsonify(result)