# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492442.951973
_enable_loop = True
_template_filename = 'themes/smqtt/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks', 'html_translations']


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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        theme_color = context.get('theme_color', UNDEFINED)
        title = context.get('title', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        url_type = context.get('url_type', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\r\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\r\n<head>\r\n    <meta charset="utf-8">\r\n\r\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\r\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\r\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\r\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\r\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\r\n')
        __M_writer('\r\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\r\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\r\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\r\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\r\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\r\n\r\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\r\n')
        __M_writer('\r\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\r\n')
        __M_writer('\r\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\r\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\r\n')
        __M_writer('\r\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\r\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\r\n')
        __M_writer('\r\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\r\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\r\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/bulma.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/local.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/man.css" rel="stylesheet" type="text/css">\r\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\r\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\r\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\r\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\r\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\r\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul class="translations">\r\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\r\n')
        __M_writer('    </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 70, "23": 74, "24": 97, "25": 120, "26": 130, "32": 3, "61": 3, "62": 6, "63": 7, "64": 8, "65": 10, "66": 11, "67": 13, "68": 14, "69": 15, "70": 17, "71": 18, "72": 21, "73": 21, "74": 21, "75": 25, "76": 26, "77": 26, "78": 26, "79": 28, "80": 29, "81": 29, "82": 29, "83": 31, "84": 32, "85": 33, "86": 33, "87": 33, "88": 34, "89": 35, "90": 35, "91": 35, "92": 35, "93": 35, "94": 37, "95": 38, "96": 38, "97": 39, "98": 39, "99": 40, "100": 41, "101": 43, "102": 43, "103": 43, "104": 44, "105": 44, "106": 46, "107": 47, "108": 48, "109": 48, "110": 48, "111": 48, "112": 48, "113": 48, "114": 48, "115": 51, "116": 52, "117": 53, "118": 53, "119": 53, "120": 55, "121": 56, "122": 57, "123": 57, "124": 57, "125": 59, "126": 60, "127": 60, "128": 60, "129": 62, "130": 63, "131": 64, "132": 65, "133": 66, "134": 66, "135": 66, "136": 68, "137": 69, "138": 69, "144": 72, "149": 72, "150": 73, "151": 73, "157": 76, "165": 76, "166": 77, "167": 78, "168": 79, "169": 80, "170": 81, "171": 83, "172": 84, "173": 89, "174": 90, "175": 93, "176": 94, "182": 99, "193": 99, "194": 100, "195": 101, "196": 101, "197": 101, "198": 102, "199": 103, "200": 104, "201": 105, "202": 105, "203": 105, "204": 105, "205": 105, "206": 107, "207": 108, "208": 108, "209": 108, "210": 111, "211": 112, "212": 113, "213": 114, "214": 114, "215": 114, "216": 114, "217": 114, "218": 116, "219": 117, "220": 117, "221": 117, "227": 122, "237": 122, "238": 124, "239": 125, "240": 126, "241": 126, "242": 126, "243": 126, "244": 126, "245": 126, "246": 126, "247": 129, "253": 247}}
__M_END_METADATA
"""
