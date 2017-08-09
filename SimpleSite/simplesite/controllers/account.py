import logging

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn
from authkit.users.sqlalchemy_driver import UsersFromDatabase

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from simplesite.lib import helpers as h
from simplesite.lib.base import BaseController, render
from simplesite.model.meta import Session, Base

log = logging.getLogger(__name__)

class AccountController(BaseController):

	def index(self):
		return 'Hello World'

	def __before__(self):
		user = session.get('user')
		if user:
			request.environ['REMOTE_USER'] = user

	def signup(self):
		return render('account/signup.html')

	def create_user(self):
		users = request.environ['authkit.users']
		created = False
		for i in users.list_users():
			if i.encode('utf-8') == request.params['username']:
				created = True

		if created == False:
			users.user_create(request.params['username'], password=request.params['password'])
			Session.commit()
		print(users.list_users())
		c.user = 'asdf'
		# c.user = {request.params['username']: password=request.params['password']}
		return render('account/user_created.html')

	def signin(self, id="private"):
		print("singin test")
		print(id, "=====")
		if len(request.params) > 1 and request.params['username'] is not None:
			session['user'] = request.params['username']
			session.save()
			print(id, 'line 50')
			return redirect(url(controller='account', action=id))
		elif session.get('user'):
			return redirect(url(controller='account', action=id))
		else:
			return render('account/signin.html', {id:id})

	def signout(self):
		session.delete()
		return render('account/signedout.html')


	def public(self):
		return 'This is public'

	# @authorize(RemoteUser())
	def private(self):
		# for i in request.environ:
		if request.environ.get("REMOTE_USER"):
			print(request.remote_user)
			return render('private.html')
		else:
			return redirect(url(controller='account', action="signin", id='private'))

	# @authorize(h.auth.is_valid_user)
	def admin(self):
		if h.auth.authorized(h.auth.has_admin_role):
			users = request.environ['authkit.users']
			list_users = users.list_users()
			c.users = list_users
			return render('admin.html')
		return redirect(url(controller='account', action="signin", id='admin'))

