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

ld = {'url':'http://ichart.yahoo.com/table.csv?s={stock_id}&a={from_m}&b={from_d}&c={from_y}&d={to_m}&e={to_d}&f={to_y}&g={interval}&ignore=.csv','url_params':{'stock_id':'GOOG', 'from_m':'1', 'from_d':'1', 'from_y':'2007', 'to_m':'2', 'to_d':'28', 'to_y':'2012', 'interval':'w'}}


@app.route('/tests', methods=['GET','POST'])
def index():
	form = StockId(request.form)
	rd = ysk.yh_stock_api_get(ld)
	l_hist = js_plot(rd)
	curr_quote = ''
	d_last_hist = ''
	return render_template('index.html',curr_quote=curr_quote, d_last_hist_=d_last_hist,form=form, l_hist=l_hist)

def js_plot(rd):	
	l = []
	for item in rd['values']:
		tl = []
		tl.append(item[0])
		tl.append(float(item[4]))
		l.append(tl)
	return l
