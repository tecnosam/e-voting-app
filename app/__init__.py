from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import gevent
import os

app = Flask( __name__ )
app.secret_key = os.environ.get("POLLS_SECRET_KEY", "samplestuff").encode()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
socket = SocketIO( app )

db = SQLAlchemy( app )

from .models import *

# db.create_all()

from .views import *

from .app_socket import *
