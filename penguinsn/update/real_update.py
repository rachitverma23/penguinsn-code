
import handler
import webapp2


class DataRequestHandler(handler.Handler):

	def get(self):
		requested_chat = self.request.get("chat", default_value="none")
		messages  =  ffdfd