import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from simplesite.lib.base import BaseController, render
from simplesite.model import Page, Video, Tag
from simplesite.model.meta import Session

log = logging.getLogger(__name__)

class SearchController(BaseController):

	def index(self):
		string_query = request.params.get('q')
		regex = r'[a-zA-Z]+'
		string_query_filtered = re.findall(regex, string_query)
		a = ""
		for i in string_query_filtered:
			a += i + "|"
		string_query_filtered = a.encode('utf-8')

		regex=string_query_filtered[0:-1]
		print(regex)
		videos = Session.query(Video).all()
		results = []
		for video in videos:

			found = re.findall(regex, video.title, re.I|re.M)
			print(found)
			if len(found) != 0:
				results.append(video)

		return render('search/search_result.html', {'results': results})
