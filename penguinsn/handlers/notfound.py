

import webapp2 
import handler

class NotFoundHandler(handler.Handler): 
	def get(self, error ):
		self.render('notfound.html') 


