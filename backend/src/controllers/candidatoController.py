from flask import render_template, redirect, url_for, request, abort
from models.Candidato import Candidato
from flask_sqlalchemy import SQLAlchemy
# from models.schemas import *
# from app import CandidatoSchema
db = SQLAlchemy()

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

def candidatos():
    all_candidatos = Candidato.query.all()
    result = candidato_schemas.dump(all_candidatos)
    return jsonify(result)

def create_elector():
    print(request.json)
    elector_name=request.json["elector_name"]
    elector_dni=request.json["elector_dni"]
    elector_huella=request.json["elector_huella"]
    ubigeo_idUbigeo=request.json['ubigeo_idUbigeo']

    new_elector = Elector(elector_name,elector_dni,elector_huella,ubigeo_idUbigeo)

    db.session.add(new_elector)
    db.session.commit()

    return elector_schema.jsonify(new_elector)