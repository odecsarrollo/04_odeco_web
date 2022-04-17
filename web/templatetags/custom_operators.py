from django import template

register = template.Library()


@register.filter(name='carrousel_indicator_index')
def carrousel_indicator_index(value, arg):
    return int(int(value) / int(arg))


@register.simple_tag(takes_context=True)
def default_internationalization(context, espanol, ingles, default=None):
    lenguaje_actual = context.get('LANGUAGE_CODE')
    if lenguaje_actual == 'en':
        return ingles or default or espanol
    return espanol or default
