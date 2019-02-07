from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user
from app import app, config, db, forms, models
from datetime import datetime

from app import helpers

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
    gh_tag_latest = helpers.GetLatestGithubRelease(app.config['CV_GITHUB_REPO'])
    return render_template('cv.html', title='Curriculum Vitae', gh_tag_latest=gh_tag_latest, config=app.config)

@app.route('/events')
def events():
    upcoming_events = models.Event.query.filter(models.Event.date >= datetime.utcnow()).order_by(models.Event.date.asc()).all()
    past_events     = models.Event.query.filter(models.Event.date < datetime.utcnow()).order_by(models.Event.date.desc()).all()

    return render_template('events.html', title='Events', upcoming_events=upcoming_events, past_events=past_events)

@app.route('/research')
def research():
    return render_template('research.html', title='Research')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ERROR HANDLING
# .............................................................................
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
