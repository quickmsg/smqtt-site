# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492443.1394725
_enable_loop = True
_template_filename = 'themes/smqtt/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_translations', 'html_sourcelink', 'html_post_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\r\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\r\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\r\n')
            __M_writer('        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" class="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def html_translations(post):
            return render_html_translations(context,post)
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <header>\r\n')
        __M_writer('        <div class="metadata">\r\n')
        __M_writer('            <p class="dateline">\r\n        <a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time></a>\r\n')
        if post.author() != blog_author:
            if author_pages_generated:
                __M_writer('                      | <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\r\n')
            else:
                __M_writer('                      | ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\r\n')
        __M_writer('      </p>\r\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\r\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\r\n')
        if post.meta('link'):
            __M_writer('                    <p class="linkline"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\r\n')
        __M_writer('        </div>\r\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\r\n    </header>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 61, "45": 5, "51": 5, "52": 6, "53": 7, "54": 7, "55": 7, "56": 7, "57": 7, "63": 11, "72": 11, "73": 12, "74": 13, "75": 14, "76": 14, "77": 15, "78": 16, "79": 17, "80": 17, "81": 17, "82": 17, "83": 17, "84": 17, "85": 17, "86": 20, "92": 24, "99": 24, "100": 25, "101": 26, "102": 26, "103": 26, "104": 26, "105": 26, "111": 30, "127": 30, "128": 33, "129": 41, "130": 42, "131": 42, "132": 42, "133": 42, "134": 42, "135": 42, "136": 42, "137": 42, "138": 43, "139": 44, "140": 45, "141": 45, "142": 45, "143": 45, "144": 45, "145": 46, "146": 47, "147": 47, "148": 47, "149": 50, "150": 51, "151": 52, "152": 52, "153": 52, "154": 54, "155": 54, "156": 54, "157": 55, "158": 56, "159": 56, "160": 56, "161": 56, "162": 56, "163": 58, "164": 59, "165": 59, "171": 165}}
__M_END_METADATA
"""
