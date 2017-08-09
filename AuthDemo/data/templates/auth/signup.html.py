# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1502246839.559253
_enable_loop = True
_template_filename = '/home/minhpn/Documents/projects/pylons/AuthDemo/authdemo/templates/auth/signup.html'
_template_uri = 'auth/signup.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u"{% extends 'base.html' %}\n{% block title %} \nSignup{% endblock %}\n{% block content %}\n\n{{ h.form(h.url(controller='auth', action='signup'), method='post') }}\n\nUsername: {{ h.text('username')}}<br>\nPassword: {{ h.text('password')}}<br>\n\n{{ h.submit('submit', 'Submit') }}\n{{ h.end_form() }}\n{% endblock %}")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "auth/signup.html", "filename": "/home/minhpn/Documents/projects/pylons/AuthDemo/authdemo/templates/auth/signup.html"}
__M_END_METADATA
"""
