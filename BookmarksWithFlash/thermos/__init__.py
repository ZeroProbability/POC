import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from logging import DEBUG

basedir = os.path.abspath(os.path.dirname(__file__))

# configure database
app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY']='''\x04\xd2\t>[-\x06\x06\x1ar%I\xeb\x18\xd6*\x0f~\xae\xa26\x95@\xee'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

# configure authentication
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.session_protection = 'strong'
login_manager.init_app(app)

import views
import models
