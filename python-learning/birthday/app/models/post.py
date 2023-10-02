from app.extensions import db

class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    birthday_id = db.Column(db.Integer, db.ForeignKey('birthday.id'))
    birthday = db.relationship('Birthday', backref='events')
