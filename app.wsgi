#!/usr/bin/python

activate_this = 'env/bin/activate_this.py'
exec(open(activate_this).read())

import sys
import logging

logging.basicConfig(stream = sys.stderr)
sys.path.insert(0, '/var/www/html')

from app import app as application
