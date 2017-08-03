import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from authtest.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ExampleController(BaseController):

    def hello(self):
    	return self._result()

    def _result(self):
    	return "Hello world"
