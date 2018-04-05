# Using "Semantic Versioning": MAJOR.MINOR.PATCH form.
# See: https://semver.org/ for more details.
__version__ = '0.2.1'


# -*- coding: utf-8 -*-
from flask import Flask
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.config['VERSION'] = __version__

from app import routes
