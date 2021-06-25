from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import time


@app.route('/login', methods=['POST'])
def login_post():
    print(request.json)

    username = request.json['usuario']
    password = request.json['contraseña']
    print(username)
    print(password)

    if username is None or password is None:
        print("user or pass is none")
        return "Falta llenar usuario o contraseña"

    if Usuario.query.filter_by(usuario_usuario = username).first() is  None or Usuario.query.filter_by(usuario_contraseña = password).first() is  None:
        print("user or pass is ready")
        rest = {
            'idRoldes': None
        }
        return jsonify(rest)
    
    user = Usuario.query.filter_by(usuario_usuario = username).first()
    passt = Usuario.query.filter_by(usuario_contraseña = password).first()
    user_auth = user.idusuario
    pass_auth = passt.idusuario


    if user == passt:
        print("usuario logeado")
        print(passt.roles_idRoles)
        freqs = {
            'idRoldes': passt.roles_idRoles
        }

        return jsonify(freqs)

    else:
        print("contraseña o usuario equivocado") 
        rest = {
            'idRoldes': None
        }
        return jsonify(rest)
