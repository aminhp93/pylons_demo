
import logging
import jinja2demo.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from jinja2demo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FormsetController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/formset.mako')
        # or, return a string
        return 'Hello World'

    def form(self):
    	
    	return render('simpleform.html')

    def submit(self):	
    	h.redirect(url(controller='formset', action='result'))

    def result(self):
		return 'Your email is %s' % "minh@gmail.com"
