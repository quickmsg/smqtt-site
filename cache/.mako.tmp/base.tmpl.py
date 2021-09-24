# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492442.9185972
_enable_loop = True
_template_filename = 'themes/smqtt/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

    ns = runtime.TemplateNamespace('annotations', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'annotations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        footer = _mako_get_namespace(context, 'footer')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        header = _mako_get_namespace(context, 'header')
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body class="layout-documentation page-grid">\r\n    ')
        __M_writer(str(header.html_header()))
        __M_writer('\r\n    <div class="container">\r\n         <main id="content">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n         </main>\r\n    </div>\r\n    <br/>\r\n    <br/>\r\n    <br/>\r\n    ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\r\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n    ')
        __M_writer(str(body_end))
        __M_writer('\r\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 0, "57": 2, "58": 3, "59": 4, "60": 5, "61": 6, "62": 6, "63": 7, "64": 7, "69": 10, "70": 11, "71": 11, "72": 14, "73": 14, "78": 17, "79": 23, "80": 23, "81": 24, "82": 24, "87": 25, "88": 26, "89": 26, "90": 27, "91": 27, "97": 8, "107": 8, "113": 17, "128": 25, "143": 128}}
__M_END_METADATA
"""
