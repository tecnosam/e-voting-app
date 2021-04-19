from pollaris_ import app, socket
from flask import render_template, flash, request, redirect, url_for
from pollaris_ import controllers as ctr


@app.route("/aspirants", methods = ['GET', 'POST', 'DELETE'])
def aspirants():

	if request.method == 'POST':

		pid = request.form['pid']
		fname = request.form['fname']
		lname = request.form['lname']
		ctr.add_aspirant( fname, lname, pid )
	elif request.method == 'DELETE':

		id = request.args['id']
		# print(id)
		ctr.delete_aspirant( id )
		return "true"

	return render_template( "aspirants.html" )

@app.route( "/results", methods = ['GET', 'POST'] )
def results_view():

	return render_template( "results.html", positions = ctr.positions_with_asp() )

@app.route( "/vote", methods = ['GET', 'POST'] )
def vote_view():
	if request.method == 'POST':

		ballot = dict(request.form)

		for pid in ballot:
			if ballot[ pid ] != 0:
				# append voters count
				socket.emit("add-vote", 

					ctr.count_vote( pid, asp = ballot[ pid ] ),
					broadcast=True)

				print( f"LOG: ballot casted for {pid}" )

		flash( "Successfully posted result", "success" )

	return render_template( "vote.html", positions = ctr.positions_with_asp() )

@app.route("/positions", methods = ['GET', 'POST'])
def positions_view():
	if request.method == 'POST':

		pos = request.form['pos']
		if ( 'edit-pos' in request.args ):
			ctr.edit_position( request.args['edit-pos'], pos )
		else:
			ctr.add_position( pos )

		return redirect( url_for("aspirants") )



	return render_template( "pos.html", positions = ctr.positions_with_asp() )

