
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from app import app, login_manager

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    selected_blue = db.Column(db.Integer, default=-1)
    blue_coins = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.id

    def get_id(self):
        return self.id

    def is_active():
        return (True)

    def is_authenticated(self):
        return (True)

class BlueStuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sprite = db.Column(db.String)
    attack_name = db.Column(db.String)
    damage = db.Column(db.Integer)
    userid = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return '<Blue %r>' % self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
