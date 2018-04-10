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
    return render_template('code.html', title='Code')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/cv')
def cv():
    return render_template('cv.html', title='Curriculum Vitae')

@app.route('/events')
def events():
    return render_template('events.html', title='Events')

@app.route('/research')
def research():
    return render_template('research.html', title='Research')



# ERROR HANDLING
# .............................................................................
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
