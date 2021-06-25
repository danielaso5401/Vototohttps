from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import models.Elector_has_Candidato

class Elector(db.Model):
    id_elector = db.Column(db.Integer, primary_key=True)
    elector_name = db.Column(db.String(100))
    elector_dni = db.Column(db.String(8))
    elector_image = db.Column(db.String(1000))
    # elector_image=db.Column(db.LargeBinary)
    ubigeo_idUbigeo = db.Column(db.Integer,db.ForeignKey('ubigeo.idubigeo'),nullable=False)
    electores_cantidato = db.relationship('Elector_has_Candidato', backref='elector', lazy=True)

    def __init__(self,elector_name,elector_dni,elector_image,ubigeo_idUbigeo):
        self.elector_name=elector_name
        self.elector_dni=elector_dni
        self.elector_image=elector_image
        self.ubigeo_idUbigeo = ubigeo_idUbigeo