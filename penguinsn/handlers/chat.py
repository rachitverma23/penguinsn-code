
import webapp2 
import models 
import handler

from google.appengine.ext import db 

class ChatHandler(handler.Handler):
	def render_index(self, user='', text='', error=''):
		chat_script = db.GqlQuery("SELECT * FROM ChatScript ORDER BY timestamp DESC") 
		
		# We dont want to perform the query above to the database again and again for 
		# iteration so we turn it into an iteratable object 

		#Lookup the User's coordinates from their IP 
		# Generate the User's Location from static maps

		self.render('index.html', user=user, text=text, 
			error=error, 
			chat_script=chat_script)  

	def get(self):
		self.render_index() 

	def post(self):
		text = self.request.get('text')
		name = self.request.get('username')  

		if text and name:
			transcript_data = models.ChatScript(text=text, user=name) 
			transcript_data.put()                     
			self.redirect('/')
		else:
			error = 'WE NEED SOME TEXT IN HERE, PLEASE'
			self.render_index(name, text, error) 