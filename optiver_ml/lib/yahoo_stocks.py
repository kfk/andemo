import urllib2 
import calendar, time

def curr_quote(stock_id):
	header = ['name','id','open','close']
	url = 'http://download.finance.yahoo.com/d/quotes.csv?s='+stock_id+'&f=nsop&e=.csv'
	data = urllib2.urlopen(url)
	d = {}
	l = []
	for item in data:
		n = -1
		td = {}
		item = item.replace('"','')
		item = item.split(',')
		for k in header:
			n+=1
			td[k] = item[n]
		l.append(td)
	d['sorted_keys'] = header
	d['data'] = l
	return d
import datetime

def hist_quote(stock_id):
	header = ['date','open', 'close']
	d = {'stock_id':stock_id, 'from_m':'1', 'from_d':'1', 'from_y':'2007', 'to_m':'2', 'to_d':'28', 'to_y':'2012', 'interval':'w'}
	url = 'http://ichart.yahoo.com/table.csv?s={stock_id}&a={from_m}&b={from_d}&c={from_y}&d={to_m}&e={to_d}&f={to_y}&g={interval}&ignore=.csv'.format(**d)
	data = urllib2.urlopen(url)
	l = []
	l_last = []
	d_last = {}
	n = -1
	for row in data:
		n+=1
		if n >= 1:
			tl = []
			row = row.split(',')
			time = row[0].split('-')
			time = calendar.timegm((int(time[0]),int(time[1]),int(time[2]),0,0,0,0,0))*1000
			tl.append(time) 
			tl.append(float(row[-1]))
			l.append(tl)
			
			n2 = -1
			td = {}
			for k in header:
				n2+=1
				td[k] = row[n2]	
			td['&Delta;'] = '%.2f' % (float(td['open'])-float(td['close'])) 
			td['&Delta;%'] = '%.2f' % (float(td['&Delta;'])/float(td['open'])*100)
			l_last.append(td)
	for item in ['&Delta;','&Delta;%']:
		header.append(item)
	d_last['data'] = l_last
	d_last['sorted_keys'] = header
	l.reverse()
	l.pop(-1)
	return l, d_last

hist_quote('GOOG')

