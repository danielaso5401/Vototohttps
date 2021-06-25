from flask import render_template, redirect, url_for, request, abort
from models.Usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# cors = CORS(app)

def create_voto():
    print(request.json)

    elector_idElector=request.json['elector_idElector']
    candidato_idCandidato=request.json['candidato_idCandidato']

    new_voto = Elector_has_Candidato(elector_idElector,candidato_idCandidato)

    db.session.add(new_voto)
    db.session.commit()

    return electorCandidato_schema.jsonify(new_voto)

def reporte_voto(id):
    print(request.json)

    elector_idElector=request.json['elector_idElector']
    candidato_idCandidato=request.json['candidato_idCandidato']

    new_voto = Elector_has_Candidato(elector_idElector,candidato_idCandidato)

    db.session.add(new_voto)
    db.session.commit()

    return electorCandidato_schema.jsonify(new_voto)

def reporte_votos():
    print(request.json)

    elector_idElector=request.json['elector_idElector']
    candidato_idCandidato=request.json['candidato_idCandidato']

    new_voto = Elector_has_Candidato(elector_idElector,candidato_idCandidato)

    db.session.add(new_voto)
    db.session.commit()

    return electorCandidato_schema.jsonify(new_voto)