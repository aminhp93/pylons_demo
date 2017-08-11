# import logging

# from pylons import request, response, session, tmpl_context as c, url
# from pylons.controllers.util import abort, redirect

# from simplesite.lib.base import BaseController, render

# from simplesite.model import Video

# log = logging.getLogger(__name__)

# class VideosController(BaseController):
#     """REST Controller styled on the Atom Publishing Protocol"""
#     # To properly map this controller, ensure your config/routing.py
#     # file has a resource setup:
#     #     map.resource('video', 'videos')

#     def index(self, format='html'):
#         """GET /videos: All items in the collection"""
#         # url('videos')
#         videos = Video.select()
#         if format == 'json':
#             data = []
#             for video in videos:
#                 d = video._state['original'].data
#                 del d['password']
#                 d['title'] = url('video', id=video.title)
#                 data.append(d)
#             response.headers['content-type'] = 'text/javascript'
#             return dumps(data)
#         else:
#             c.videos = videos
#             # return render('/videos/index_video.mako')
#             return render('/videos/index_video.html')

#     def create(self):
#         """POST /videos: Create a new item"""
#         # url('videos')

#     def new(self, format='html'):
#         """GET /videos/new: Form to create a new item"""
#         # url('new_video')

#     def update(self, id):
#         """PUT /videos/id: Update an existing item"""
#         # Forms posted to this method should contain a hidden field:
#         #    <input type="hidden" name="_method" value="PUT" />
#         # Or using helpers:
#         #    h.form(url('video', id=ID),
#         #           method='put')
#         # url('video', id=ID)

#     def delete(self, id):
#         """DELETE /videos/id: Delete an existing item"""
#         # Forms posted to this method should contain a hidden field:
#         #    <input type="hidden" name="_method" value="DELETE" />
#         # Or using helpers:
#         #    h.form(url('video', id=ID),
#         #           method='delete')
#         # url('video', id=ID)

#     def show(self, id, format='html'):
#         """GET /videos/id: Show a specific item"""
#         # url('video', id=ID)

#     def edit(self, id, format='html'):
#         """GET /videos/id/edit: Form to edit an existing item"""
#         # url('edit_video', id=ID)
