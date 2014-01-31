
import webapp2 
import models 
import handler
from penguinsn.parse import location

from google.appengine.ext import db 

class ChatHandler(handler.Handler):
	def render_index(self, user='', text='', error=''):
		chat_script = db.GqlQuery(
			"SELECT * " 
			"FROM ChatScript "  
			"ORDER BY timestamp DESC ") ;

		chat_script = list(chat_script)

		points = filter(None, (c.coords for c in chat_script))
		img_url = None 
		if points:
			img_url = location.image_url(points)
		# We dont want to perform the query above to the database again and again for 
		# iteration so we turn it into an iteratable object 

		self.render('index.html', user=user, text=text, 
			error=error, 
			chat_script=chat_script,
			img_url=img_url)  

	def get(self):
		self.render_index()  

	def post(self):
		text = self.request.get('text')
		name = self.request.get('username')  

		if text and name:
			transcript_data = models.ChatScript(text=text, user=name) 
			coords = location.get_coords(self.request.remote_addr)
			# Generate the User's Location from static maps
			if coords:
				transcript_data.coords = coords 
			transcript_data.put()                     
			self.redirect('/')
		else:
			error = 'WE NEED SOME TEXT IN HERE, PLEASE'
			self.render_index(name, text, error) 

