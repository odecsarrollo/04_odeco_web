from django import template
from web_soluciones.models import Solucion

register = template.Library()


@register.inclusion_tag('web/base/cabezote_botones_soluciones.html')
def botones_soluciones():
    Soluciones = Solucion.objects.all().order_by('orden')
    return {
        'soluciones_list': Soluciones
    }
