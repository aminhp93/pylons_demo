import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from jinja2demo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ExampleController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/example.mako')
        # or, return a string
        context = {"hello": "hello"}
        c.var = context
        return render('simpleform.html')
