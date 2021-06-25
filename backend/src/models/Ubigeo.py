from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import models.Elector

class Ubigeo(db.Model):
    idubigeo = db.Column(db.Integer, primary_key=True)
    ubigeo_departamento= db.Column(db.String(45))
    electores = db.relationship('Elector', backref='ubigeo', lazy=True)

    def __init__(self,ubigeo_departamento):
        self.ubigeo_departamento= ubigeo_departamento