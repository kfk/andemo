from optiver_ml import app
from optiver_ml.lib import yahoo_stocks as ysk
from flask import render_template, request, jsonify
from wtforms import Form, BooleanField, TextField, validators

import json 

class Stock_id(Form):
    stock_id = TextField('stock_id', [validators.Length(min=4, max=10)])

dh = {'url':'http://ichart.yahoo.com/table.csv?s={stock_id}&a={from_m}&b={from_d}&c={from_y}&d={to_m}&e={to_d}&f={to_y}&g={interval}&ignore=.csv','url_params':{'stock_id':'GOOG', 'from_m':'1', 'from_d':'1', 'from_y':'2007', 'to_m':'2', 'to_d':'28', 'to_y':'2012', 'interval':'w'}, 'trans_fs':{'to_unix_timestamp'}}

dc = {'name':'values','url':'http://download.finance.yahoo.com/d/quotes.csv?s={stock_id}&f=nsop&e=.csv','url_params':{'stock_id':'GOOG'},'header':['name','id','open','close']}

@app.route('/', methods=['GET','POST'])
def index():
	form = Stock_id(request.form)
	names = {}
	l_hist = {}
	if request.method == 'POST':
		dh['url_params']['stock_id'] = form.stock_id.data
		dc['url_params']['stock_id'] = form.stock_id.data
	names['stock_id'] = '"'+dc['url_params']['stock_id']+'"'
	rd = ysk.yh_stock_api_get(dh)
	curr_quote = ysk.d_to_html_table(ysk.yh_stock_api_get(dc))
	table_hist = ysk.d_to_html_table(rd, table_id='dynamic_table')
	return render_template('index.html',curr_quote=curr_quote,form=form,table_hist=table_hist,names=names)

@app.route('/stock')
def stock():
	return render_template('stock.html')

#From here Json Api
import calendar
@app.route('/js_plot/<stock_id>')
def js_plot_t(stock_id):	
	print stock_id
	dh['url_params']['stock_id']=stock_id
	rd = ysk.yh_stock_api_get(dh)
	l = []
	lm1 = []
	n = -1
	m1 = 10
	m  = [2,3,4]
	acc1 = 0
	for item in rd['values']:
		n+=1
		tl = []
		item_s = item[0].split('-')
		tm = calendar.timegm((int(item_s[0]),int(item_s[1]),int(item_s[2]),0,0,0,0,0))*1000
		tl.append(tm)
		tl.append(float(item[4]))
		l.append(tl)
		tl = []
		if n<m1:
			acc1+=float(item[4])
		if n == m1:
			tl.append(tm)
			tl.append(acc1/m1)
			lm1.append(tl)
			n=-1
			acc1=0
	j = {}
	j['lm1']={'label':'mav_test', 'data':lm1}
	j['aa_stock']={'label':stock_id,'data':l}
	return jsonify(j)

@app.route('/get_last_quote')
def get_last_quote():
	last_quote = ysk.yh_stock_api_get(dc)
	t = {}
	t['aaData'] = last_quote['values']
	#t['aaData'] = [["q","b","c"]]
	return jsonify(t)

