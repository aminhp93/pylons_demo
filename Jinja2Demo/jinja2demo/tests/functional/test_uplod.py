from jinja2demo.tests import *

class TestUplodController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='uplod', action='index'))
        # Test response...
