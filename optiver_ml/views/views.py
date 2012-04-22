from optiver_ml import app
from flask import render_template, request
from wtforms import Form, BooleanField, TextField, validators

@app.route('/tests')
def tests():
	return str(app.config['EPIO_DATA_DIRECTORY'])

def clean_string(string):
	for item in ['\n']:
		string = string.replace(item,'')
	return string
@app.route('/financials/csvLoad', methods=['GET','POST'])
def fin_csvLoad():
	if request.method=='POST':
		fl = request.files['file']
		fl_l=fl.readlines()
		dataset = open(app.config['finDataLoc'],'r').readlines()
		entityLoad = fl_l[0].split(',')[0]
		out=''
		for row in dataset:
			print row
			if row.split(',')[0]!=entityLoad:
				out+=row
		for row in fl_l:
			out+=clean_string(row)+'\n'
		open(app.config['finDataLoc'],'w').write(out)
	return render_template('tcsvLoad.html')
