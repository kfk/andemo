import urllib2 
import calendar, time

def tran_f(item):
	print item
	item = item.split('-')
	item = calendar.timegm((int(item[0]),int(item[1]),int(item[2]),0,0,0,0,0))*1000
	return item

def yh_stock_api_get(d):
	'Gets a hash table with url and url params: {url_1:{param1:xyz,parm2:zvx}}'
	rd = {}
	try:
		rd['header'] = d['header']
	except KeyError:
		rd['header']=False
		
	url = d['url'].format(**d['url_params'])
	data = urllib2.urlopen(url)
	l = []
	n = -1
	for row in data:
		n+=1
		row = row.split(',')
		if rd['header'] != False:	
			row[0] = tran_f(row[0])
			l.append(row)
		else:
			if n>0:
				row[0] = tran_f(row[0])
				l.append(row)
			else:
				rd['header'] = row
	rd['values'] = l
	return rd

def d_to_html_table(d, table_id=''):
	out_h = ''
	for item in d['header']:
		out_h += '''<th>{}</th>\n'''.format(item)

	out_b = ''	
	for row in d['values']:
		out_b+='<tr>\n'
		for item in row:	
			out_b+='<td>{}</td>\n'.format(item)
		out_b+='</tr>\n'
	html_table = '''<table class='table table-bordered table-striped' id='''+table_id+'''>''' + '<thead>' + out_h +'</thead>' + '<tbody>' + out_b + '</tbody>' + '</table>\n'
	return html_table

#ld = {'name':'values','url':'http://download.finance.yahoo.com/d/quotes.csv?s={stock_id}&f=nsop&e=.csv','url_params':{'stock_id':'GOOG'},'header':['name','id','open','close']}
ld = {'url':'http://ichart.yahoo.com/table.csv?s={stock_id}&a={from_m}&b={from_d}&c={from_y}&d={to_m}&e={to_d}&f={to_y}&g={interval}&ignore=.csv','url_params':{'stock_id':'GOOG', 'from_m':'1', 'from_d':'1', 'from_y':'2007', 'to_m':'2', 'to_d':'28', 'to_y':'2012', 'interval':'w'}}

