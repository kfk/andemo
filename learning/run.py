import re

class calcRows:
	'Creates calculated dict keys based on string formula. It requires that all the keyes used in the formula exist in the hash table'	
	def __init__(self):
		self.entity = ''
		self.map_data()

	def map_data(self):
		file_dat = open('data.dat','r').read()

		d={}
		for row in file_dat.split('\n'):
			row = row.split(',')
			if row != ['']:
				d[(row[0],row[1])] = row[2:]
		
		f ='001-002+003'	
		self.entity = 'entity1'
		rgx = re.sub(r'([0-9]+)',r'float(d[\1][i])',f)
		rgx = re.sub(r'([0-9]+)',self.repl,rgx)
	
		print d
		for i in range(6):
			print eval(rgx)	
	
		return d

	def repl(self,matchobj):
		j = '("'+self.entity +'","'+ matchobj.group(0)+'")'
		return j



calcRows()
		
