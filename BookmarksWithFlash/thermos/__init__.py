import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY']='''\x04\xd2\t>[-\x06\x06\x1ar%I\xeb\x18\xd6*\x0f~\xae\xa26\x95@\xee'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

from thermos import models
from thermos import views
