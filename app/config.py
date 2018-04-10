# -*- coding: utf-8 -*-
__author__ = 'Justin Vasel'
import os

# Basics
BASEDIR      = os.path.abspath(os.path.dirname(__file__))

# DATABASE
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data/app.db')
SQLALCHEMY_ECHO         = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Google Analytics
GATRACKINGID = 'UA-109768490-2'
