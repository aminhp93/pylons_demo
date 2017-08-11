from simplesite.tests import *

class TestVideosController(TestController):

    def test_index(self):
        response = self.app.get(url('videos'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url('formatted_videos', format='xml'))

    def test_create(self):
        response = self.app.post(url('videos'))

    def test_new(self):
        response = self.app.get(url('new_video'))

    def test_new_as_xml(self):
        response = self.app.get(url('formatted_new_video', format='xml'))

    def test_update(self):
        response = self.app.put(url('video', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url('video', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url('video', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url('video', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url('video', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url('formatted_video', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url('edit_video', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url('formatted_edit_video', id=1, format='xml'))
