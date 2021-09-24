# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1632492442.9832208
_enable_loop = True
_template_filename = 'themes/smqtt/templates/base_footer.tmpl'
_template_uri = 'base_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


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
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if content_footer:
            __M_writer('  <footer id="footer" class="finalfooter">\r\n    <div class="container">\r\n      <div class="content has-text-centered">\r\n        <div class="footerlink is-centered">\r\n          <a href="https://github.com/quickmsg/smqtt">Github</a>\r\n          <a href="https://gitee.com/quickmsg/mqtt-cluster">Gitee</a>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </footer>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/smqtt/templates/base_footer.tmpl", "uri": "base_footer.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 17, "40": 4, "47": 4, "48": 5, "49": 6, "55": 49}}
__M_END_METADATA
"""
