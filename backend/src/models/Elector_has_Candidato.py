from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Elector_has_Candidato(db.Model):
    idElector_Candidato = db.Column(db.Integer, primary_key=True)
    elector_idElector = db.Column(db.Integer,db.ForeignKey('elector.id_elector'),nullable=False)
    candidato_idCandidato = db.Column(db.Integer,db.ForeignKey('candidato.idCandidato'),nullable=False)

    def __init__(self, elector_idElector, candidato_idCandidato):
        self.elector_idElector = elector_idElector
        self.candidato_idCandidato = candidato_idCandidato