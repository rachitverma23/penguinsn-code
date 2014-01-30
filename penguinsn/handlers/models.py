

from google.appengine.ext import db

class ChatScript(db.Model):

	text = db.TextProperty(required=True)
	user = db.StringProperty(required=True)
	timestamp = db.DateTimeProperty(auto_now_add=True)
	coords = db.GeoPtProperty() 