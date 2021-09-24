# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.3582237
_enable_loop = True
_template_filename = 'D:/nikola/lib/site-packages/nikola/data/themes/base/templates/comments_helper_utterances.tmpl'
_template_uri = 'comments_helper_utterances.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        utterances_config = context.get('utterances_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('" id="utterances-thread"></div>\n        <script src="https://utteranc.es/client.js" repo="')
            __M_writer(str(comment_system_id))
            __M_writer('"\n')
            if utterances_config:
                for k, v in utterances_config.items():
                    __M_writer('        ')
                    __M_writer(str(k))
                    __M_writer('="')
                    __M_writer(str(v))
                    __M_writer('"\n')
            __M_writer('        ></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#utterances-thread">')
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
{"filename": "D:/nikola/lib/site-packages/nikola/data/themes/base/templates/comments_helper_utterances.tmpl", "uri": "comments_helper_utterances.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 13, "22": 19, "23": 23, "29": 2, "35": 2, "36": 3, "37": 4, "38": 4, "39": 4, "40": 5, "41": 5, "42": 6, "43": 7, "44": 8, "45": 8, "46": 8, "47": 8, "48": 8, "49": 11, "55": 15, "61": 15, "62": 16, "63": 17, "64": 17, "65": 17, "66": 17, "67": 17, "73": 22, "77": 22, "83": 77}}
__M_END_METADATA
"""
