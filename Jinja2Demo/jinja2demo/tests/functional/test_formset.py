from jinja2demo.tests import *

class TestFormsetController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='formset', action='index'))
        # Test response...
