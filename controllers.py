from flask_restful import fields, marshal_with
from pollaris_ import db
from pollaris_.models import AspirantModel, PositionModel

aspirant_field = {
	"id": fields.Integer,
	"pid": fields.String,
	'fname': fields.String,
	'lname': fields.String,
	'votes': fields.Integer
}

@marshal_with( aspirant_field )
def all_aspirants(pid):
	# data = AspirantModel.query.all()
	data = AspirantModel.query.filter_by( pid = pid ).all()
	return data

@marshal_with({"id": fields.Integer, "pos": fields.String})
def all_positions():
	data = PositionModel.query.all()
	res = []

	return data

def positions_with_asp(  ):
	positions = all_positions()
	for row in positions:
		row.aspirants = all_aspirants( row['id'] )
		# res.append( row )
	return positions

@marshal_with({ "id": fields.Integer, "votes": fields.Integer })
def count_vote( pid, asp ):
	aspirant = AspirantModel.query.filter_by( pid = pid, id = asp ).first()
	if aspirant:
		aspirant.votes += 1
		db.session.commit()
	return aspirant

def add_aspirant( fname, lname, pid ):
	aspirant = AspirantModel( fname = fname, lname = lname, pid = pid )
	db.session.add( aspirant )
	db.session.commit()
	return

def add_position( pos ):
	aspirant = PositionModel( pos = pos )
	db.session.add( aspirant )
	db.session.commit()

def delete_aspirant( id ):
	res = AspirantModel.query.filter_by( id = id ).delete()
	db.session.commit()

def edit_position( pid, pos ):
	position = PositionModel.query.filter_by( id = pid ).first()

	if position:
		position.pos = pos
		db.session.commit()
