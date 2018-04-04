from flask import render_template, redirect, request

from app import app

# - - - Routes - - -
# .............................................................................
@app.route('/')
def index():
    return render_template('maintenance.html', title = 'Maintenance')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/code')
def code():
    return render_template('code.html')
