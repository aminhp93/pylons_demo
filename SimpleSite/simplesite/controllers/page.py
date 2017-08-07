import logging
import formencode
from formencode import htmlfill

from simplesite.lib import helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

from simplesite.model import Page, Video
from simplesite.lib.base import BaseController, render
from simplesite.model.meta import Session


log = logging.getLogger(__name__)

class NewPageForm(formencode.Schema):
	allow_extra_fields = True
	filter_extra_fields = True
	title = formencode.validators.String(not_empty=True)
	content = formencode.validators.String(not_empty=True)

class PageController(BaseController):

	def __before__(self):
		self.page_q = Session.query(Page)

	def list(self):
		c.pages = self.page_q
		c.paginator = h.paginate.Page(
			c.pages,
			page=int(request.params.get('page', 1)),
			items_per_page = 1,
		)
		return render('page/list.html')

	def show(self, id=None):
		if id is None:
			abort(404)
		c.page = self.page_q.get(int(id))
		if c.page is None:
			abort(404)
		
		return render('page/show.html')

	def new(self):
		c.videos = Session.query(Video)
		return render('page/new.html')

	@validate(schema=NewPageForm(), form='new')
	def create(self):
		page = Page()
		for k, v in self.form_result.items():
			setattr(page, k, v)
		video = Session.query(Video).filter_by(id=request.params['video_id']).first()
		if video is None:
			abort(404)
		page.videos.append(video)
		Session.add(page)
		Session.commit()
		return redirect(url(controller='page', action='list'))

	def edit(self, id=None):
		if id is None:
			abort(404)
		page = self.page_q.filter_by(id=id).first()
		if page is None:
			abort(404)
		values = {
			'title': page.title,
			'content': page.content
		}
		c.title = page.title
		return htmlfill.render(render('page/edit.html'), values)

	@validate(schema=NewPageForm(), form='edit')
	def save(self, id=None):
		page = self.page_q.filter_by(id=id).first()
		if page is None:
			abort(404)
		for k, v in self.form_result.items():
			if getattr(page, k) != v:
				setattr(page, k, v)
		Session.commit()

		return redirect(url(controller='page', action='show', id=page.id))

	def delete(self, id=None):
		if id is None:
			abort(404)
		page = self.page_q.filter_by(id=id).first()
		if page is None:
			abort(404)
		Session.delete(page)
		Session.commit()
		return render('page/deleted.html')



