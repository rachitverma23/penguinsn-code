
import handler
import webapp2
from google.appengine.ext import db

class DataRequestHandler(handler.Handler):

	def get(self):
		requested_chat = self.request.get("chat", default_value="none")
		messages  =  db.GqlQuery("SELET * FROM ChatScript WHERE CHAT = :1 ORDER BY timestamp", 
					requested_chat).fetch(20)
		self.render('update.json', msg_list=messages, chat=requested_chat, 
				time=self.request.get("time", default_value=0))
		self.response.headers["Content-Type"] = "application/xml" 
		self.response.headers.add_header("Access-Control-Allow-Origin", "*") 
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")

