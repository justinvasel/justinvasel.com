# Using "Semantic Versioning": MAJOR.MINOR.PATCH form.
# See: https://semver.org/ for more details.
__version__ = '1.0.0'


# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['VERSION'] = __version__

db = SQLAlchemy(app)

from app import models
from app import routes

db.create_all()
db.session.commit()
