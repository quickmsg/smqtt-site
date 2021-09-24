# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.2175937
_enable_loop = True
_template_filename = 'themes/smqtt/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


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
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        parent = context.get('parent', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\r\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\r\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\r\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\r\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\r\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
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
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\r\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\r\n    <div class="content">\r\n    ')
        __M_writer(str(post.text()))
        __M_writer('\r\n    </div>\r\n    <aside class="postpromonav">\r\n    <nav>\r\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\r\n    </nav>\r\n    </aside>\r\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\r\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\r\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\r\n        </section>\r\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\r\n</article>\r\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "55": 2, "56": 3, "57": 4, "58": 5, "59": 6, "64": 27, "69": 50, "75": 8, "85": 8, "86": 9, "87": 9, "88": 10, "89": 11, "90": 11, "91": 11, "92": 14, "93": 15, "94": 15, "95": 15, "96": 15, "97": 15, "98": 17, "99": 18, "100": 18, "101": 18, "102": 18, "103": 18, "104": 20, "105": 21, "106": 23, "107": 23, "108": 23, "109": 24, "110": 24, "111": 25, "112": 25, "113": 26, "114": 26, "120": 29, "133": 29, "134": 30, "135": 30, "136": 31, "137": 31, "138": 33, "139": 33, "140": 37, "141": 37, "142": 38, "143": 38, "144": 41, "145": 42, "146": 43, "147": 43, "148": 44, "149": 44, "150": 47, "151": 47, "152": 47, "153": 49, "154": 49, "160": 154}}
__M_END_METADATA
"""
