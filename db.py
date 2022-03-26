
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    selected_blue = db.Column(db.Integer, default=-1)

    def __repr__(self):
        return '<User %r>' % self.id

class BlueStuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sprite = db.Column(db.String)
    attack_name = db.Column(db.String)
    damage = db.Column(db.Integer)
    userid = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return '<Blue %r>' % self.id
