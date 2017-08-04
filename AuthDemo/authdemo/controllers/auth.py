import logging

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from authdemo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AuthController(BaseController):
	# @authorized(ValidAuthKitUser())
	# def __before__(self):
	# 	pass

	def private(self):
		print("1")
		
		for i in request.environ:
			print(i, "|||", request.environ[i])
		if request.environ.get('REMOTE_USER'):
			print("2")
			return "Authenticated"
		else:

			print("3")
			response.status = "401 Not Authenticated"
			return "You are not authenticated"

	# @authorize(RemoteUser())
	# # @authorize(UserIn(['amin']))
	# def private(self):
	# 	return "You are authenticated!"

	def signout(self):
		return "Signed out"

	def public(self):
		
		return "This is still only visible when you are signed in."
