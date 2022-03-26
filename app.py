
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, static_folder="static/")

app.secret_key = 'super secret key'

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blue.db'

#login
login_manager = LoginManager()
login_manager.init_app(app)
