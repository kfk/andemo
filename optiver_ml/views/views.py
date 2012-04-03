from optiver_ml import app
from optiver_ml.lib import yahoo_stocks as ysk
from flask import render_template, request

from wtforms import Form, BooleanField, TextField, validators

class StockId(Form):
    stockId = TextField('StockId', [validators.Length(min=4, max=10)])

@app.route('/', methods=['GET','POST'])
def index():
	form = StockId(request.form)
	d = ysk.curr_quote('GOOG')
	l_hist, d_last_hist = ysk.hist_quote('GOOG')
	curr_quote = d_to_html(d)
	d_last_hist = d_to_html(d_last_hist, table_id="'dynamic_table'")
	if request.method == 'POST':
		stockId = form.stockId.data
		d = ysk.curr_quote(stockId)
		l_hist, d_last_hist = ysk.hist_quote(stockId)
		d_last_hist = d_to_html(d_last_hist, table_id="'dynamic_table'")
		curr_quote = d_to_html(d)
		return render_template('index.html', form=form, curr_quote=curr_quote, l_hist=l_hist, d_last_hist=d_last_hist)
 
	return render_template('index.html', form=form, curr_quote=curr_quote,l_hist=l_hist, d_last_hist=d_last_hist)

def d_to_html(d, table_id=''):	
	out_h = ''
	for k in d['sorted_keys']:
		out_h += '''<th>{}</th>\n'''.format(k)
	
	out_b = ''	
	for row in d['data']:
		out_b+='<tr>\n'
		for k in d['sorted_keys']:	
			out_b+='<td>{}</td>\n'.format(row[k])
		out_b+='</tr>\n'
	html_table = '''<table class='table table-bordered table-striped' id='''+table_id+'''>''' + '<thead>' + out_h +'</thead>' + '<tbody>' + out_b + '</tbody>' + '</table>\n'
	return html_table
