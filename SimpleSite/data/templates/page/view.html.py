# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501819443.6973341
_enable_loop = True
_template_filename = '/home/minhpn/Documents/projects/pylons/SimpleSite/simplesite/templates/page/view.html'
_template_uri = 'page/view.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u"{% extends 'base/index.html' %}\n\n{% block content %}\nTests\n{% endblock %}")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "page/view.html", "filename": "/home/minhpn/Documents/projects/pylons/SimpleSite/simplesite/templates/page/view.html"}
__M_END_METADATA
"""
