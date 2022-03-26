
from flask import Flask

app = Flask(__name__, static_folder="static/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blue.db'
