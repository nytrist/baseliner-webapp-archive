from flask import Flask, render_template, url_for

app  = Flask(__name__)

@app.route('/') # active sensor stations with gateway and link to readings
def home():
	return render_template('index.html')

@app.route('/stations') # all active gateways with their linked sensor stations
def get_gateways():
	return render_template('stations.html')

@app.route('/station/<ss_id>') # individual sensor stations
def get_station(ss_id):
	return render_template('station.html', ss_id=ss_id)

@app.route('/readings') #all readings
def get_readings():
	return render_template('readings.html')

@app.route('/add') #add gateway / add or update node
def add():
	return render_template('add.html')

@app.route('/delete') #add gateway
def delete():
	return render_template('delete.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5050, debug=True)
