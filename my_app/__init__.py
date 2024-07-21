import os
from flask import Flask

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

from pathlib import Path

from dotenv import load_dotenv
dotenv_path = Path(__file__).parent.parent.joinpath('.env')
load_dotenv(dotenv_path)

DB_HOST = os.getenv("DB_HOST")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_HOST

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_migrate import Migrate
Migrate(app, db)

from my_app.models import *
import my_app.views
