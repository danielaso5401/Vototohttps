from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import models.Usuario

class Roles(db.Model):
    idroles = db.Column(db.Integer, primary_key=True)
    roles_descripcion = db.Column(db.String(100))
    roles=db.relationship('Usuario', backref='roles',lazy=True)
    def __init__(self, roles_descripcion):
        self.roles_descripcion=roles_descripcion