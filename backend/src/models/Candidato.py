from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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

