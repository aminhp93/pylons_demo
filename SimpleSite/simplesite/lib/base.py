"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_jinja2 as render

from simplesite.model.meta import Session
from pylons import session, request

class BaseController(WSGIController):

	def __call__(self, environ, start_response):
		"""Invoke the Controller"""
		# WSGIController.__call__ dispatches to the Controller method
		# the request is routed to. This routing information is
		# available in environ['pylons.routes_dict']
		try:
			user = session.get('user')
			if user:
				request.environ['REMOTE_USER'] = user
			return WSGIController.__call__(self, environ, start_response)
		finally:
			Session.remove()
