from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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