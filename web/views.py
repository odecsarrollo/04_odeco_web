from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'web/index.html'

class SolucionView(TemplateView):
    template_name = 'web/soluciones/solucion_detail.html'
