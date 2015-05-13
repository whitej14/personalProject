from urllib2 import urlopen
from json import load
from flask import Flask, render_template
# http://localhost:5000/search/lat/long/
app = Flask(__name__)

#g.latitude = 0.0
#g.longitude = 0.0

@app.route("/search/<string:lat>/<string:lon>/") #/search/lat/long/
def search(lat, lon):
	#g.longitude = lon
	#g.latitude = lat

	randomness = "lat: %s lon: %s" % (lat, lon)
	lat_lon = "%s,%s" % (lat,lon) 
	
	key = "AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo"

	url = 'https://maps.googleapis.com/maps/api/place/search/json?location='
	url = url + lat_lon
	url = url + '&radius=500&sensor=true&keyword=hospital&key='
	url = url + key
	response = urlopen(url)
	json_obj = load(response)
	list_n = json_obj['results'][0:4]

	reference_num = list()
	all_phonenum = list()

	for place in list_n:
		reference_num.append(place['reference'])

	for reference in reference_num:
		url = 'https://maps.googleapis.com/maps/api/place/details/json?reference='
		url = url + reference
		url = url + '&radius=500&sensor=true&keyword=hospital&key='
		url = url + key
		response = urlopen(url)
		json_obj = load(response)
		all_phonenum.append(json_obj['result']['formatted_phone_number'])

	return render_template('contacts_pg.html', places = list_n, numbers = all_phonenum)


@app.route('/')
def getLocation():
	return render_template('gpslocator.html')
		
	#return render_template('contacts_pg.html', places = list_n, numbers = all_phonenum)

	#return render_template('map_pg.html')
	#hospital_addresses=all_addresses, hospital_numbers=all_phonenum

#@app.route('/')
#def getLocation():
	#return render_template('gpslocator.html')

#@app.route('/map_pg')
#def linktomap():
	#render_template('map_pg.html')

#@app.route("/map_pg")
#def get_map():
	#key = "AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo"
	#url = 'http://maps.googleapis.com/maps/api/staticmap?center='
	#url = url + str(g.latitude) + ',' + str(g.longitude)
	#url = url + '&zoom=14&size=400x400&sensor=false&key='
	#url = url + key 37.42291810/-122.08542120/
	#maps = url
	#return render_template('map_pg.html', maps=maps)
	
#http://maps.googleapis.com/maps/api/staticmap?center=37.80674930910263,-122.27011963221332&zoom=14&size=400x400&sensor=false&key=AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
#http:// IP address:5000
#1. / geolocation javascript: handle function should connect to another flask url: /q?lat=50&long=50
#2. /q   get info from lat and long and print it out
#3. stick it as google place location variable
#https://maps.googleapis.com/maps/api/place/search/json?location=37.80674930910263,-122.27011963221332&radius=500&sensor=true&key=AIzaSyDdxVDEz0tAVh6199Rz-fjZnp4h2Sf-rIo
#render Christina's template to get my variables printed 
