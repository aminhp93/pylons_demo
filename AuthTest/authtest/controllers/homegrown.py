import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from authtest.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HomegrownController(BaseController):

    def __before__(self, action, **params):
    	user = session.get('user')
    	print(session)
    	print(user)
    	print(params)
    	print(request)
    	# print(request.environ['REMOTE_USER'])
    	if user:
    		request.environ['REMOTE_USER'] = user

    def signin(self):
    	if len(request.params) > 1 and request.params['password'] == request.params['username']:
    		session['user'] = request.params['username']
    		session.save()
    		return redirect(url(controller='homegrown',action='private'))
    	else:
    		return """
			<html>
                 <head><title>Please Login!</title></head>
                 <body>
                   <h1>Please Login</h1>
                   <form action="signin" method="post">
                     <dl>
                       <dt>Username:</dt>
                       <dd><input type="text" name="username"></dd>
                       <dt>Password:</dt>
                       <dd><input type="password" name="password"></dd>
                     </dl>
                     <input type="submit" name="authform" />
                     <hr />
                   </form>
                 </body>
               </html
    		"""
    		
    def public(self):
    	return "This is public"

    def private(self):
    	if request.environ.get("REMOTE_USER"):
    		return "This is private"
    	else:
    		return redirect(url(controller="homegrown", action="signin"))
