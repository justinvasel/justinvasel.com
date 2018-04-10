from app import db

# .............................................................................
class Event(db.Model):
    __tablename__ = 'events'
    id           = db.Column(db.Integer(), primary_key = True)
    date         = db.Column(db.Date())
    description  = db.Column(db.Text())
    location     = db.Column(db.String())
    name         = db.Column(db.String())
    type         = db.Column(db.Integer(), db.ForeignKey('eventtypes.id'))

class EventType(db.Model):
    __tablename__ = 'eventtypes'
    id           = db.Column(db.Integer(), primary_key = True)
    name         = db.Column(db.String())
