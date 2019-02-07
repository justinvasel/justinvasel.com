# -*- coding: utf-8 -*-
__author__ = 'Justin Vasel'
import os

# Basics
BASEDIR      = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = ''

# DATABASE
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data/app.db')
SQLALCHEMY_ECHO         = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CV
CV_GITHUB_REPO = 'justinvasel/curriculum-vitae'
CV_FILENAME    = 'jvasel_cv.pdf'

# Google Analytics
GATRACKINGID = 'UA-109768490-2'
