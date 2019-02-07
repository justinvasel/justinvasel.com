# Using "Semantic Versioning": MAJOR.MINOR.PATCH form.
# See: https://semver.org/ for more details.
__version__ = '2.0.1'


# -*- coding: utf-8 -*-
from flask import Flask, redirect
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['VERSION'] = __version__

db = SQLAlchemy(app)

login = LoginManager()
login.init_app(app)
login.login_view = 'login'
from app import routes

from app import models
db.create_all()
db.session.commit()

## FLASK ADMIN ##
class AdminHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect('/')
        return self.render('admin/index.html')

class AdminView(ModelView):
    column_display_pk = True
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(app, template_mode='bootstrap3', index_view=AdminHomeView())
admin.add_view(AdminView(models.Event, db.session))
admin.add_view(AdminView(models.EventType, db.session))
admin.add_view(AdminView(models.EventTypeQualifier, db.session))
admin.add_view(AdminView(models.User, db.session))
