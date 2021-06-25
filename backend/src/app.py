from flask import Flask, render_template
from flask_restful import Resource, Api
# from flask_migrate import Migrate
from flask_misaka import Misaka
from models.Usuario import db
from routers.candidato_bp import candidato_bp
from routers.elector_bp import elector_bp
from routers.login_bp import login_bp
from routers.roles_bp import roles_bp
from routers.ubigeo_bp import ubigeo_bp
from routers.usuario_bp import usuario_bp
from routers.voto_bp import voto_bp
# from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

# ma = Marshmallow(app)

# migrate = Migrate(app, db)

# app(login_bp)

# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()