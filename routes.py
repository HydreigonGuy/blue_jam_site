
from crypt import methods
from flask import jsonify, redirect, render_template, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from db import BlueStuff, User, db
from game import summon_blue_stuff

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if (user and user.password == request.form.get('password')):
            login_user(user)
            return redirect("/")
        return render_template("login.html", error_message="Incorrect User or Password")
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if (user):
            return render_template("register.html", error_message="User already exists")
        newUser = User(username=username, password=request.form.get('password'), blue_coins=1000)
        db.session.add(newUser)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@app.route('/game/')
def game():
    if not current_user.is_authenticated:
        return redirect("/login")
    return render_template("game/home.html")

@app.route('/game/summon', methods=['GET', 'POST'])
@login_required
def game_summon():
    if request.method == 'POST':
        res = {
            'message':'',
            'blue_coins':current_user.blue_coins,
            'img':''
        }
        if current_user.blue_coins < 100:
            res['message'] = 'Not enough Blue Coins'
        else:
            user = User.query.filter_by(id=current_user.id).first()
            summon = summon_blue_stuff(user.id)
            db.session.add(summon)
            user.blue_coins -= 100
            db.session.commit()
            res['blue_coins'] = user.blue_coins
            res['message'] = 'Congratulations, you have summoned a ' + summon.name
            res['img'] = summon.sprite
        return jsonify(res)
    return render_template("game/summon.html", user=current_user)

@app.route('/game/blue_guys')
def game_blue_guys():
    blue_guys = BlueStuff.query.filter_by(userid=current_user.id).all()
    return render_template("game/home.html")
