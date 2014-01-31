
import requests 
from google.appengine.ext import db

URL = 'http://www.geobytes.com/IpLocator.htm?GetLocation&template=json.txt&IpAddress='
STATIC_MAPS_URL = 'http://maps.googleapis.com/maps/api/staticmap?sensor=false&size=526x321&'

def get_coords(ip):
	try:
		content = requests.get(URL+ip).json()
	except URLError:
		return 
	if content:
		lat = content['geobytes']['latitude']
		lon = content['geobytes']['longitude']

	return db.GeoPt(lat, lon)

def image_url(points):
	points = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in points) 
	return STATIC_MAPS_URL + points 