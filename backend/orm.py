from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import request
from flask import jsonify

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@127.0.0.1:5432/sistema_votacionV2"
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
    elector_huella = db.Column(db.String(100))
    ubigeo_idUbigeo = db.Column(db.Integer,db.ForeignKey('ubigeo.idubigeo'),nullable=False)
    electores_cantidato = db.relationship('Elector_has_Candidato', backref='elector', lazy=True)

    def __init__(self,elector_name,elector_dni,elector_huella,ubigeo_idUbigeo):
        self.elector_name=elector_name
        self.elector_dni=elector_dni
        self.elector_huella=elector_huella
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
    