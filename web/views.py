from django.views.generic import TemplateView

from web_empresa.models import Aliado
from web_clientes.models import Cliente


class IndexView(TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aliados_list'] = Aliado.objects.all()
        context['clientes_list'] = Cliente.objects.all().order_by('orden')
        return context


class SolucionView(TemplateView):
    template_name = 'web/soluciones/solucion_detail.html'
