# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.0769706
_enable_loop = True
_template_filename = 'themes/smqtt/templates/story.tmpl'
_template_uri = 'story.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\r\n    <header>\r\n')
        __M_writer('        ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\r\n    </header>\r\n    <div class="content">\r\n    ')
        __M_writer(str(post.text()))
        __M_writer('\r\n    </div>\r\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('        <section class="comments">\r\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\r\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\r\n        </section>\r\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\r\n</article>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/story.tmpl", "uri": "story.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "52": 2, "53": 3, "54": 4, "55": 5, "56": 6, "61": 25, "67": 8, "80": 8, "81": 9, "82": 9, "83": 12, "84": 12, "85": 12, "86": 15, "87": 15, "88": 17, "89": 18, "90": 19, "91": 19, "92": 20, "93": 20, "94": 23, "95": 23, "96": 23, "102": 96}}
__M_END_METADATA
"""
