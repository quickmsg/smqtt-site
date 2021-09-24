# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492442.9832208
_enable_loop = True
_template_filename = 'themes/smqtt/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_translation_header():
            return render_html_translation_header(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <header id="header">\r\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\r\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\r\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\r\n                ')
            __M_writer(str(search_form))
            __M_writer('\r\n            </div>\r\n')
        __M_writer('        ')
        __M_writer(str(html_site_title()))
        __M_writer('\r\n    </header>\r\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if (post and post.title):
            __M_writer('    <section class="hero">\r\n      <div class="hero-body is-paddingless">\r\n      <div class="container has-text-centered">\r\n')
            if title == blog_title:
                __M_writer('        <h1 class="title">SMQTT™</h1>\r\n        <h2 class="subtitle">An open source MQTT broker</h2>\r\n')
            elif post and post.title:
                __M_writer('        <h1 class="title" itemprop="headline name">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</h1>\r\n')
            __M_writer('      </div>\r\n    </div>\r\n    <hr>\r\n  </section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n  <script>\r\ndocument.addEventListener(\'DOMContentLoaded\', function () {\r\n\r\n  // Get all "navbar-burger" elements\r\n  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll(\'.navbar-burger\'), 0);\r\n\r\n  // Check if there are any navbar burgers\r\n  if ($navbarBurgers.length > 0) {\r\n\r\n    // Add a click event on each of them\r\n    $navbarBurgers.forEach(function ($el) {\r\n      $el.addEventListener(\'click\', function () {\r\n\r\n        // Get the target from the "data-target" attribute\r\n        var target = $el.dataset.target;\r\n        var $target = document.getElementById(target);\r\n\r\n        // Toggle the class on both the "navbar-burger" and the "navbar-menu"\r\n        $el.classList.toggle(\'is-active\');\r\n        $target.classList.toggle(\'is-active\');\r\n\r\n      });\r\n    });\r\n  }\r\n\r\n});</script>\r\n  <div class="container">\r\n    <nav class="navbar" role="navigation" aria-label="main navigation">\r\n      <div class="navbar-brand">\r\n        <a class="navbar-item" href="https://smqtt.org/">\r\n          <img src="/images/smqtt-text-side-28.png" alt="SMQTT: An Open Source MQTT Broker" width="139" height="28">\r\n        </a>\r\n        <button class="button navbar-burger" data-target="navMenu">\r\n          <span></span>\r\n          <span></span>\r\n          <span></span>\r\n        </button>\r\n      </div>\r\n      <div class="navbar-menu" id="navMenu">\r\n        <div class="navbar-end">\r\n\r\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('      <div class="navbar-item has-dropdown is-hoverable">\r\n        <a class="navbar-link">')
                __M_writer(str(text))
                __M_writer('</a>\r\n        <div class="navbar-dropdown">\r\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <a class="navbar-item" href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\r\n')
                    else:
                        __M_writer('                     <a class="navbar-item" href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\r\n')
                __M_writer('        </div>\r\n      </div>\r\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <a class="navbar-item" href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\r\n')
                else:
                    __M_writer('                <a class="navbar-item" href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\r\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\r\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\r\n\r\n        </div>\r\n      </div>\r\n       </nav>\r\n    <hr style="margin-top: 0rem">\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\r\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\r\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 16, "35": 34, "36": 108, "37": 117, "43": 4, "57": 4, "58": 6, "59": 6, "60": 7, "61": 7, "62": 8, "63": 9, "64": 10, "65": 10, "66": 13, "67": 13, "68": 13, "69": 15, "70": 15, "76": 18, "85": 18, "86": 19, "87": 20, "88": 23, "89": 24, "90": 26, "91": 27, "92": 27, "93": 27, "94": 29, "100": 36, "113": 36, "114": 78, "115": 79, "116": 80, "117": 81, "118": 81, "119": 83, "120": 84, "121": 85, "122": 85, "123": 85, "124": 85, "125": 85, "126": 86, "127": 87, "128": 87, "129": 87, "130": 87, "131": 87, "132": 90, "133": 92, "134": 93, "135": 94, "136": 94, "137": 94, "138": 94, "139": 94, "140": 95, "141": 96, "142": 96, "143": 96, "144": 96, "145": 96, "146": 100, "147": 100, "148": 100, "149": 101, "150": 101, "156": 110, "166": 110, "167": 111, "168": 112, "169": 113, "170": 113, "171": 114, "172": 114, "178": 172}}
__M_END_METADATA
"""
