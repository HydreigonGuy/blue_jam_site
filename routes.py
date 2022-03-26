
from flask import render_template
from app import app
from db import BlueStuff

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/game/')
def game():
    return render_template("game/home.html")

@app.route('/game/blue_guys')
def game():
    #blue_guys = BlueStuff.query.filter_by(userid= current user id )
    return render_template("game/home.html")
