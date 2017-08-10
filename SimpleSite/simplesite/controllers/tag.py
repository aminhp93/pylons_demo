import logging
import formencode
from formencode import htmlfill

from simplesite.lib import helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

from simplesite.model import Tag, Association, Video
from simplesite.lib.base import BaseController, render
from simplesite.model.meta import Session


log = logging.getLogger(__name__)

class NewTagForm(formencode.Schema):
	allow_extra_fields = True
	filter_extra_fields = True
	content = formencode.validators.String(not_empty=True)

class TagController(BaseController):

	def __before__(self):
		self.tag_q = Session.query(Tag)

	def list(self):
		c.tags = self.tag_q
		return render('tag/list.html')

	def show(self, id=None):
		if id is None:
			abort(404)
		tag = self.tag_q.get(int(id))
		if tag is None:
			abort(404)
		return render('tag/show.html', {'tag': tag})

	def new(self):
		a = ExpiringTokenGenerator()
		b = a.generate_token()
		print(b)
		return render('tag/new.html')

	@validate(schema=NewTagForm(), form='new')
	def create(self):
		tag = Tag()
		for k, v in self.form_result.items():
			setattr(tag, k, v)

		Session.add(tag)
		Session.commit()
		return redirect(url(controller='tag', action='list'))

	def edit(self, id=None):
		if id is None:
			abort(404)
		tag = self.tag_q.filter_by(id=id).first()
		if tag is None:
			abort(404)
		values = {
			'content': tag.content,
		}

		return htmlfill.render(render('tag/edit.html', {'tag': tag.content}), values)

	@validate(schema=NewTagForm(), form='edit')
	def save(self, id=None):
		tag = self.tag_q.filter_by(id=id).first()
		if tag is None:
			abort(404)
		for k, v in self.form_result.items():
			if getattr(tag, k) != v:
				setattr(tag, k, v)
		Session.commit()

		return redirect(url(controller='tag', action='show', id=tag.id))

	def delete(self, id=None):
		if id is None:
			abort(404)
		tag = self.tag_q.filter_by(id=id).first()
		if tag is None:
			abort(404)
		Session.delete(tag)
		Session.commit()
		return render('tag/deleted.html')


	def related(self, content=None):
		tag_id = Session.query(Tag).filter_by(content=request.params['content']).first()
		# association = Session.query(Association).filter_by(tag_id=tag_id.id).first()
		
		associations = Session.query(Association).filter_by(tag_id=tag_id.id)
		video_list = []
		for association in associations:
			video = Session.query(Video).filter_by(id=association.video_id).first()
			video_list.append(video)

		print(video_list)

		return render('tag/related_result.html', {'video_list': video_list})



