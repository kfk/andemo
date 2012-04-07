import urllib2 
import calendar, time

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
			l.append(row)
		else:
			if n>0:
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

