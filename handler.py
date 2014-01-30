
import webapp2
import jinja2 
import os 

template_dir = os.path.join(os.path.dirname(__file__), 'webpages')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
			autoescape=True)

class Handler(webapp2.RequestHandler):

	def write(self, *a, **kwa):
		self.response.out.write(*a, **kwa)  

	def render_str(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kwa):
		self.write(self.render_str(template, **kwa))