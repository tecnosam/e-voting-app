from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask( __name__ )
app.secret_key = os.environ.get("POLLS_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

socket = SocketIO( app )

db = SQLAlchemy( app )

from pollaris_.models import *

# db.create_all()

from pollaris_.views import *