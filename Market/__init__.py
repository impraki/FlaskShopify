from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c650217f6f4fae7a7e47ad66'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Market import routes
