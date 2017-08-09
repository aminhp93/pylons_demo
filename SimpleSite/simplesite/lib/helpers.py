"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from simplesite.lib import auth
from webhelpers.html.tags import *
import webhelpers.paginate as paginate

from pylons import url
from webhelpers.pylonslib import Flash as _Flash
flash = _Flash()

