
def map_data():
	file_dat = open('data.dat','r').read()

	d={}
	for row in file_dat.split('\n'):
		row = row.split(',')
		if row != ['']:
			d[(row[0],row[1])] = row[2:]
	return d

		
