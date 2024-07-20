import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path(__file__).parent.parent.joinpath('.env')
load_dotenv(dotenv_path)

DB_HOST = os.getenv("DB_HOST")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_HOST

db = SQLAlchemy(app)

Migrate(app, db)

from models import *
import views


if __name__ == 'main':
  app.run(debug=True)
