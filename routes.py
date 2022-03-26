
from flask import redirect, render_template, request
from flask_login import current_user, login_user, logout_user
from app import app
from db import BlueStuff, User, db

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
    return render_template("game/home.html")

@app.route('/game/blue_guys')
def game_blue_guys():
    blue_guys = BlueStuff.query.filter_by(userid=current_user.id).all()
    return render_template("game/home.html")
