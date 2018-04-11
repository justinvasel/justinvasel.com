from flask import render_template, redirect, request
from app import app, models, db
from datetime import datetime

# - - - Routes - - -
# .............................................................................
# FOR MAINTENANCE ONLY
# @app.route('/')
# def index():
#     return render_template('maintenance.html', title = 'Maintenance')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cat')
def cat():
    return render_template('cat.html', title='CAT!')

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
    upcoming_events = db.session.query(models.Event, models.EventType).join(models.EventType, models.EventType.id == models.Event.type).filter(models.Event.date >= datetime.utcnow()).order_by(models.Event.date.asc()).all()

    past_events = db.session.query(models.Event, models.EventType).join(models.EventType, models.EventType.id == models.Event.type).filter(models.Event.date < datetime.utcnow()).order_by(models.Event.date.desc()).all()

    return render_template('events.html', title='Events', upcoming_events=upcoming_events, past_events=past_events)

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
