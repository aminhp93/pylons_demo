import logging

from authdemo.lib import helpers as h
from authdemo.lib.base import BaseController, render
from authdemo.model.meta import Session, Base

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn
from authkit.users.sqlalchemy_driver import UsersFromDatabase

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

log = logging.getLogger(__name__)

class AuthController(BaseController):
	# @authorized(ValidAuthKitUser())
	def __before__(self):
		user = session.get('user')
		if user:
			request.environ['REMOTE_USER'] = user

	def signout(self):
		# del session['user']
		session.delete()
		return render('auth/signout.html')

	def signup(self):
		return render('auth/signup.html')

	def create_user(self):
		users = request.environ['authkit.users']
		# print(dir(users))
		# print(users.list_users()[0])
		# print(type(users.list_users()[0].encode('utf-8')))
		created = False
		for i in users.list_users():
			if i.encode('utf-8') == request.params['username']:
				created = True

		if created == False:
			users.user_create(request.params['username'], password=request.params['password'])
			Session.commit()
		c.user = 'asdf'
		# c.user = {request.params['username']: password=request.params['password']}
		return render('auth/user_created.html')

	def signin(self):
		if len(request.params) > 1 and request.params['username'] is not None:
			session['user'] = request.params['username']
			session.save()
			return redirect(url(controller='auth', action="private"))
		elif session.get('user'):
			return redirect(url(controller='auth', action="private"))
		else:
			return render('auth/signin.html')

	def public(self):
		# print(h.auth.is_valid_user)
		# print(dir(h.auth.is_valid_user))
		# print(h.auth.authorized(h.auth.is_valid_user))
		return 'This is public'

	def private(self):
		# for i in request.environ:
			# print(i, request.environ[i])
		if request.environ.get("REMOTE_USER"):
			# print(request.environ.get('REMOTE_USER'))
			# print(request.environ['authkit.config']['form.authenticate.user.data'])
			return 'This is private'
		else:
			return redirect(url(controller='auth', action="signin"))

	@authorize(h.auth.is_valid_user)
	def admin(self):
		return "This is admin page"

	# @authorize(RemoteUser())
	# def private1(self):
		# print("==================")

	# 	return "You are authenticated!"