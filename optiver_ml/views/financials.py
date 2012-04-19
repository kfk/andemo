from optiver_ml import app
from optiver_ml.lib.lfinancials import financials_grid 
from flask import jsonify, render_template

@app.route('/financials')
def financials():
	return render_template('tfinancials.html')

@app.route('/financials_json')
def financials_json():
	d = financials_grid()
	return jsonify(d)
