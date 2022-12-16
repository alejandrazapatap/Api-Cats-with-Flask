from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3://sitio.db'

db.init_app(app)

