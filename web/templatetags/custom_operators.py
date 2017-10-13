from django import template

register = template.Library()


@register.filter(name='carrousel_indicator_index')
def carrousel_indicator_index(value, arg):
    return int(int(value) / int(arg))
