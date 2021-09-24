# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.4051294
_enable_loop = True
_template_filename = 'themes/smqtt/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

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
        def content():
            return render_content(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        index_file = context.get('index_file', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
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
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\r\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
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
        comments = _mako_get_namespace(context, 'comments')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        index_teasers = context.get('index_teasers', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\r\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\r\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\r\n')
        __M_writer('<div class="postindex">\r\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\r\n    <header>\r\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\r\n        <div class="metadata">\r\n')
            __M_writer('            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\r\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\r\n')
            __M_writer('        </div>\r\n    </header>\r\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\r\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\r\n')
            else:
                __M_writer('    <div class="e-content entry-content">\r\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\r\n')
            __M_writer('    </div>\r\n\t<hr>\r\n    </article>\r\n')
        __M_writer('</div>\r\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\r\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "67": 2, "68": 3, "69": 4, "70": 5, "71": 6, "76": 14, "81": 57, "87": 8, "98": 8, "99": 9, "100": 9, "101": 10, "102": 11, "103": 11, "104": 11, "105": 13, "106": 13, "107": 13, "113": 16, "135": 16, "140": 17, "141": 18, "142": 19, "143": 19, "144": 19, "145": 21, "146": 22, "147": 22, "148": 22, "149": 24, "150": 25, "151": 26, "152": 26, "153": 26, "154": 28, "155": 28, "156": 28, "157": 28, "158": 37, "159": 37, "160": 37, "161": 37, "162": 37, "163": 37, "164": 37, "165": 37, "166": 37, "167": 38, "168": 39, "169": 39, "170": 39, "171": 41, "172": 43, "173": 44, "174": 45, "175": 45, "176": 46, "177": 47, "178": 48, "179": 48, "180": 50, "181": 54, "182": 55, "183": 55, "184": 56, "185": 56, "191": 17, "202": 191}}
__M_END_METADATA
"""
