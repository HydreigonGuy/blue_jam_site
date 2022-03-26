
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
def game_blue_guys():
    #blue_guys = BlueStuff.query.filter_by(userid= current user id )
    return render_template("game/home.html")

@app.route('/music/')
def music():
    return render_template("music/home.html")

@app.route('/perso/')
def perso():
    return render_template("perso/home.html")

@app.route('/defi/')
def defi():
    return render_template("defi/home.html")