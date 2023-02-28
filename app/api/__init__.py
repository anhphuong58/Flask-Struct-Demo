from flask import Flask
from app import login_manager
from app.api import notify, auth_api
from flask_login import LoginManager
from app.models.user import *
def register_blueprints(app: Flask):
    app.register_blueprint(notify.bp, url_prefix='/api')
    app.register_blueprint(auth_api.auth, url_prefix='/')





@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))