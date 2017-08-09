import logging
import formencode
from formencode import htmlfill

from simplesite.lib import helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

from simplesite.model import Video, Tag, Association
from simplesite.lib.base import BaseController, render
from simplesite.model.meta import Session


log = logging.getLogger(__name__)

class NewVideoForm(formencode.Schema):
	allow_extra_fields = True
	filter_extra_fields = True
	title = formencode.validators.String(not_empty=True)
	url = formencode.validators.String(not_empty=True)

class VideoController(BaseController):

	def __before__(self):
		self.video_q = Session.query(Video)

	def list(self):
		c.videos = self.video_q
		return render('video/list.html')

	def show(self, id=None):
		if id is None:
			abort(404)
		c.video = self.video_q.get(int(id))
		if c.video is None:
			abort(404)
		return render('video/show.html')

	def new(self):
		tags = Session.query(Tag).all()
		return render('video/new.html', {'tags': tags})

	@validate(schema=NewVideoForm(), form='new')
	def create(self):
		video = Video()
		for k, v in self.form_result.items():
			setattr(video, k, v)

		tag_list = request.params.getall('tag_id')
		for tag_id in tag_list:
			tag = Session.query(Tag).filter_by(id=tag_id).first()
			video.tags.append(tag)

		Session.add(video)
		Session.commit()
		return redirect(url(controller='video', action='list'))

	def edit(self, id=None):
		if id is None:
			abort(404)
		video = self.video_q.filter_by(id=id).first()
		if video is None:
			abort(404)
		values = {
			'title': video.title,
			'url': video.url
		}
		c.title = video.title
		return htmlfill.render(render('video/edit.html'), values)

	@validate(schema=NewVideoForm(), form='edit')
	def save(self, id=None):
		video = self.video_q.filter_by(id=id).first()
		if video is None:
			abort(404)
		for k, v in self.form_result.items():
			if getattr(video, k) != v:
				setattr(video, k, v)
		Session.commit()

		return redirect(url(controller='video', action='show', id=video.id))

	def delete(self, id=None):
		if id is None:
			abort(404)
		video = self.video_q.filter_by(id=id).first()
		if video is None:
			abort(404)
		Session.delete(video)
		Session.commit()
		return render('video/deleted.html')



