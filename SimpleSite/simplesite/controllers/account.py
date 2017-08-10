import logging

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn
from authkit.users.sqlalchemy_driver import UsersFromDatabase

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from simplesite.lib import helpers as h
from simplesite.lib.base import BaseController, render
from simplesite.model.meta import Session, Base
from simplesite.model import User

log = logging.getLogger(__name__)

class AccountController(BaseController):

	def signup(self):
		return render('account/signup.html')

	def create_user(self):
		users = request.environ['authkit.users']
		if users.user_exists(request.params['username']) is False:
			users.user_create(request.params['username'], password=request.params['password'])
			Session.commit()
		c.user = request.params['username']
		return render('account/user_created.html')

	def signin(self):
		users = request.environ['authkit.users']
		if len(request.params) > 1 and request.params.get('username') is not None and request.params.get('password') is not None:
			if users.user_exists(request.params['username']):
				if users.user_has_password(request.params['username'], password=request.params['password']):
					session['user'] = request.params['username']
					session.save()
					return redirect(url(controller='account', action='private'))
		elif session.get('user'):
			return redirect(url(controller='account', action='private'))
		return render('account/signin.html')

	def signout(self):
		session.delete()
		return render('account/signedout.html')

	def public(self):
		return 'This is public'

	# @authorize(RemoteUser())
	def private(self):
		if request.environ.get("REMOTE_USER"):
			return render('private.html')
		else:
			return redirect(url(controller='account', action="signin"))

	@authorize(h.auth.has_admin_role)
	def admin(self):
		# if h.auth.authorized(h.auth.has_admin_role):
		users = Session.query(User).all()		
		return render('admin.html', {'users': users})

	@authorize(h.auth.has_admin_role)
	def show_user(self, id=None):
		if id is None:
			abort(404)
		user = Session.query(User).filter_by(uid=id).first()
		if user is None:
			abort(404)
		return render('admin.html')

	@authorize(h.auth.has_admin_role)
	def edit_user(self, id=None):
		if id is None:
			abort(404)
		user = Session.query(User).filter_by(uid=id).first()
		if user is None:
			abort(404)
		return render('admin.html')

	@authorize(h.auth.has_admin_role)
	def delete_user(self, id=None):
		if id is None:
			abort(404)
		user = Session.query(User).filter_by(uid=id).first()
		if user is None:
			abort(404)
		Session.delete(user)
		Session.commit()
		return render('admin.html')
