#!/usr/bin/env python

import webapp2
from penguinsn.handlers import chat
from penguinsn.handlers import notfound

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([('/', chat.ChatHandler),
								(PAGE_RE, notfound.NotFoundHandler)], debug=True)
