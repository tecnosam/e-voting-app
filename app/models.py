from . import db
from flask_restful import fields, marshal_with

class PositionModel(db.Model):
	id = db.Column( db.Integer, primary_key = True )
	pos = db.Column( db.String(100), nullable = False )

class AspirantModel( db.Model ):
	id = db.Column( db.Integer, primary_key = True )
	pid = db.Column( db.Integer, nullable = False )
	fname = db.Column( db.String(100), nullable = False )
	lname = db.Column( db.String(100), nullable = False )
	votes = db.Column( db.Integer, default = 0, nullable = False )
