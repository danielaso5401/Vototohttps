from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, send_from_directory
from sqlalchemy import text
# from flask_migrate import Migrate

# from werkzeug.security import generate_password_hash, check_password_hash, secure_filename
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import os
import time

from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

# from flask_login import UserMixins
# from .auth import auth as auth_blueprint

UPLOAD_FOLDER = os.path.abspath("/Users/cesaradolfolauramamani/Downloads/Docuentos2/python/Imgs")
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "pdf", "jpeg"])
dbConnection = "dbname='sistema_votacionV2' user='postgres' host='localhost' password='postgres'"
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)
app = Flask(__name__)
cors = CORS(app)
# cadena de coneccion
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:brethnaroot93@127.0.0.1:3306/new_schema'
# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# app.config['UPLOAD_FOLDER']= " /Imgs"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@127.0.0.1:5432/sistema_votacionesV3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # par q no de warnings

db = SQLAlchemy(app)
ma = Marshmallow(app)




class Roles(db.Model):
    idroles = db.Column(db.Integer, primary_key=True)
    roles_descripcion = db.Column(db.String(100))
    roles=db.relationship('Usuario', backref='roles',lazy=True)
    def __init__(self, roles_descripcion):
        self.roles_descripcion=roles_descripcion


class Usuario(db.Model):
    idusuario = db.Column(db.Integer, primary_key=True)
    usuario_name = db.Column(db.String(100))
    usuario_usuario = db.Column(db.String(100))
    usuario_contraseña = db.Column(db.String(100))
    roles_idRoles = db.Column(db.Integer,db.ForeignKey('roles.idroles'),nullable=False)
    def __init__(self, usuario_name, usuario_usuario, usuario_contraseña,roles_idRoles):
        self.usuario_name = usuario_name
        self.usuario_usuario = usuario_usuario
        self.usuario_contraseña = usuario_contraseña
        self.roles_idRoles = roles_idRoles

class Elector(db.Model):
    id_elector = db.Column(db.Integer, primary_key=True)
    elector_name = db.Column(db.String(100))
    elector_dni = db.Column(db.String(8))
    elector_image = db.Column(db.String(1000))
    ubigeo_idUbigeo = db.Column(db.Integer,db.ForeignKey('ubigeo.idubigeo'),nullable=False)
    electores_cantidato = db.relationship('Elector_has_Candidato', backref='elector', lazy=True)

    def __init__(self,elector_name,elector_dni,elector_image,ubigeo_idUbigeo):
        self.elector_name=elector_name
        self.elector_dni=elector_dni
        self.elector_image=elector_image
        self.ubigeo_idUbigeo = ubigeo_idUbigeo

class Ubigeo(db.Model):
    idubigeo = db.Column(db.Integer, primary_key=True)
    ubigeo_departamento= db.Column(db.String(45))
    electores = db.relationship('Elector', backref='ubigeo', lazy=True)

    def __init__(self,ubigeo_departamento):
        self.ubigeo_departamento= ubigeo_departamento

class Elector_has_Candidato(db.Model):
    idElector_Candidato = db.Column(db.Integer, primary_key=True)
    elector_idElector = db.Column(db.Integer,db.ForeignKey('elector.id_elector'),nullable=False)
    candidato_idCandidato = db.Column(db.Integer,db.ForeignKey('candidato.idCandidato'),nullable=False)

    def __init__(self, elector_idElector, candidato_idCandidato):
        self.elector_idElector = elector_idElector
        self.candidato_idCandidato = candidato_idCandidato

class Candidato(db.Model):
    idCandidato = db.Column(db.Integer, primary_key=True)
    candidato_name = db.Column(db.String(100))
    candidato_dni = db.Column(db.String(8))
    candidato_partpol = db.Column(db.String(100))
    candidato_fotocant = db.Column(db.String(100))
    candidato_fotopart = db.Column(db.String(100))
    electores_cantidato = db.relationship('Elector_has_Candidato', backref='candidato', lazy=True)


    def __init__(self, candidato_name, candidato_dni, candidato_partpol, candidato_fotocant, candidato_fotopart):
        self.candidato_name = candidato_name
        self.candidato_dni = candidato_dni
        self.candidato_partpol = candidato_partpol
        self.candidato_fotocant = candidato_fotocant
        self.candidato_fotopart = candidato_fotopart

db.create_all()

class Elector_has_CandidatoSchema(ma.Schema):
    class Meta:
        fields = ('idElector_Candidato','elector_idElector','candidato_idCandidato')

electorCandidato_schema = Elector_has_CandidatoSchema()
electorCandidato_schemas = Elector_has_CandidatoSchema(many=True)

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('idroles','roles_descripcion')

roles_schema = RolesSchema()
roles_schemas = RolesSchema(many=True)

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('idusuario','usuario_name','usuario_usuario','usuario_contraseña',"roles_idRoles")

usuario_schema = UsuarioSchema()
usuario_schemas = UsuarioSchema(many=True)

class ElectorSchema(ma.Schema):
    class Meta:
        fields = ('id_elector',"elector_name","elector_dni","elector_image","ubigeo_idUbigeo")

elector_schema = ElectorSchema()
elector_schemas = ElectorSchema(many=True)

class UbigeoSchema(ma.Schema):
    class Meta:
        fields = ("idubigeo","ubigeo_departamento")

ubigeo_schema = UbigeoSchema()
ubigeo_schemas = UbigeoSchema(many=True)

class CandidatoSchema(ma.Schema):
    class Meta:
        fields = ("idCandidato","candidato_name", "candidato_dni", "candidato_partpol", "candidato_fotocant", "candidato_fotopart")

candidato_schema = CandidatoSchema()
candidato_schemas = CandidatoSchema(many=True)

# @auth.route('/login')
# def login():
#     return render_template('login.html')


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
        # abort(400)
    if Usuario.query.filter_by(usuario_usuario = username).first() is  None or Usuario.query.filter_by(usuario_contraseña = password).first() is  None:
        print("user or pass is ready")
        rest = {
            'idRoldes': None
        }
        return jsonify(rest)
  
    #     # abort(400)
        
    user = Usuario.query.filter_by(usuario_usuario = username).first()
    passt = Usuario.query.filter_by(usuario_contraseña = password).first()
    # user = User.query.filter_by(email=email).first()
    # db.session.add(user)
    # db.session.commit()
    # usuarios()
    # user = Usuario.query.filter_by(usuario_usuario=usuario).first()
    user_auth = user.idusuario
    pass_auth = passt.idusuario
    # print(user)

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
    


@app.route('/create_voto', methods=['POST'])
def create_voto():
    print(request.json)

    elector_idElector=request.json['elector_idElector']
    candidato_idCandidato=request.json['candidato_idCandidato']

    new_voto = Elector_has_Candidato(elector_idElector,candidato_idCandidato)

    db.session.add(new_voto)
    db.session.commit()

    return electorCandidato_schema.jsonify(new_voto)

@app.route('/create_roles', methods=['POST'])
@cross_origin()
def create_roles():
    print(request.json)

    roles_descripcion = request.json['roles_descripcion']
    new_rol = Roles(roles_descripcion)
    db.session.add(new_rol)
    db.session.commit()

    return roles_schema.jsonify(new_rol)

@app.route('/get_roles', methods=['GET'])
@cross_origin()
def roles():
    all_roles = Roles.query.all()
    result = roles_schemas.dump(all_roles)
    return jsonify(result)

@app.route('/create_usuario', methods=['POST'])
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

@app.route('/get_usuario', methods=['GET'])
def usuarios():
    all_usuarios = Usuario.query.all()
    result = usuario_schemas.dump(all_usuarios)
    return jsonify(result)

@app.route('/create_elector', methods=['POST'])
def create_elector():
    print(request.json)
    elector_name=request.json["elector_name"]
    elector_dni=request.json["elector_dni"]
    elector_image=request.json["elector_image"]
    ubigeo_idUbigeo=request.json['ubigeo_idUbigeo']

    new_elector = Elector(elector_name,elector_dni,elector_image,ubigeo_idUbigeo)

    db.session.add(new_elector)
    db.session.commit()

    return elector_schema.jsonify(new_elector)

@app.route('/get_elector', methods=['GET'])
def electores():
    all_electores = Elector.query.all()
    result = elector_schemas.dump(all_electores)
    return jsonify(result)

@app.route('/get_elector/<int:id>', methods=['GET'])
def elector(id):
    post = id
    # all_electores = Elector.query.all()
    # result = elector_schemas.dump(all_electores)
    elector = User.query.get(post)
    result = elector_schemas.dump(elector)
    return jsonify(result)

@app.route('/create_ubigeo', methods=['POST'])
def create_ubigeo():
    print(request.json)
    ubigeo_departamento=request.json["ubigeo_departamento"]

    new_ubigeo = Ubigeo(ubigeo_departamento)

    db.session.add(new_ubigeo)
    db.session.commit()

    return ubigeo_schema.jsonify(new_ubigeo)

@app.route('/get_ubigeo', methods=['GET'])
def ubigeos():
    all_ubigeos = Ubigeo.query.all()
    result = ubigeo_schemas.dump(all_ubigeos)
    return jsonify(result)

@app.route('/create_candidato', methods=['POST'])
def create_candidato():
    print(request.json)
    candidato_name=request.json["candidato_name"]
    candidato_dni=request.json["candidato_dni"]
    candidato_partpol=request.json["candidato_partpol"]
    candidato_fotocant=request.json["candidato_fotocant"]
    candidato_fotopart=request.json["candidato_fotopart"]

    new_candidato = Candidato(candidato_name, candidato_dni, candidato_partpol, candidato_fotocant, candidato_fotopart)

    db.session.add(new_candidato)
    db.session.commit()

    return candidato_schema.jsonify(new_candidato)

@app.route('/get_candidato', methods=['GET'])
def candidatos():
    all_candidatos = Candidato.query.all()
    result = candidato_schemas.dump(all_candidatos)
    return jsonify(result)

@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":
        if not "file" in request.files:
            return "No file part in the form."
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # return redirect(url_for("get_file", filename=filename))
            rest = {
                'path': UPLOAD_FOLDER+"/"+filename
            }
            return jsonify(rest)
            # return UPLOAD_FOLDER+"/"+filename
        return "File not allowed."

    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Upload File</title>
</head>
<body>
    <h1>Upload File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>"""

@app.route("/uploads/<filename>")
def get_file(filename):
    print(UPLOAD_FOLDER)
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)


def main_work():
    
    # with here will take care of put connection when its done
    with getcursor() as cur:
        cur.execute("select * from \"Usuario\"")
        result_set = cur.fetchall()
        # print(result_set)

# @app.route('/get_votos', methods=['GET'])
# def candidatos():
#     # all_candidatos = Candidato.query.all()
#     # result = candidato_schemas.dump(all_candidatos)
#     result = 3
#     return jsonify(result)   

#  @app.route('/get_votos/<int:id>', methods=['GET'])
# def candidato(id):
#     id_ = id
#     result = 3
#     return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True, port=8002)
    main_work()
