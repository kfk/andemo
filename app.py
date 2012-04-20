from optiver_ml import app

app.config.update(
		DEBUG=True,
		finDataLoc='sample_data/hyp.dat',
		formuDataLoc='sample_data/hyp_conf.txt',)

if __name__=='__main__':
	app.run()
