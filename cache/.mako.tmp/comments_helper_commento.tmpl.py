# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.3582237
_enable_loop = True
_template_filename = 'D:/nikola/lib/site-packages/nikola/data/themes/base/templates/comments_helper_commento.tmpl'
_template_uri = 'comments_helper_commento.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="commento"></div>\n\n    <script defer src="')
        __M_writer(str(comment_system_id))
        __M_writer('/js/commento.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <a href="')
        __M_writer(str(link))
        __M_writer('#commento">')
        __M_writer(str(messages("Comments")))
        __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "D:/nikola/lib/site-packages/nikola/data/themes/base/templates/comments_helper_commento.tmpl", "uri": "comments_helper_commento.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 6, "22": 10, "23": 13, "29": 2, "34": 2, "35": 5, "36": 5, "42": 8, "47": 8, "48": 9, "49": 9, "50": 9, "51": 9, "57": 12, "61": 12, "67": 61}}
__M_END_METADATA
"""
