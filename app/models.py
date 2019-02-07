from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# .............................................................................
class Event(db.Model):
    __tablename__ = 'events'
    id           = db.Column(db.Integer(), primary_key = True)
    date         = db.Column(db.Date())
    description  = db.Column(db.Text())
    location     = db.Column(db.String())
    name         = db.Column(db.String())
    type_id      = db.Column(db.Integer(), db.ForeignKey('event_types.id'))
    type_qual_id = db.Column(db.Integer(), db.ForeignKey('event_type_qualifiers.id'))

    type = db.relationship('EventType', foreign_keys='Event.type_id')
    qual = db.relationship('EventTypeQualifier', foreign_keys='Event.type_qual_id')

    def __repr__(self):
        return '<Event {0}: {1}>'.format(self.id, self.name)

# .............................................................................
class EventType(db.Model):
    __tablename__ = 'event_types'
    id           = db.Column(db.Integer(), primary_key = True)
    name         = db.Column(db.String())

    def __repr__(self):
        return '<EventType {0}>'.format(self.name)

# .............................................................................
class EventTypeQualifier(db.Model):
    __tablename__ = 'event_type_qualifiers'
    id           = db.Column(db.Integer(), primary_key = True)
    name         = db.Column(db.String())

    def __repr__(self):
        return '<EventTypeQual {0}>'.format(self.name)

# .............................................................................
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer(), primary_key=True)
    username      = db.Column(db.String(),  unique=True)
    password_hash = db.Column(db.String())

    def set_password(self, password):
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {0}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
