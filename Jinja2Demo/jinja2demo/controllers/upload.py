import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from jinja2demo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UploadController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/upload.mako')
        # or, return a string
        return render('uploadform.html')

    def upload(self):
    	myfile = request.POST['myfile']
    	return "Success %s %s %s" % (myfile.filename, len(myfile.value), request.POST['description'])
    