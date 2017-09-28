from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.views.generic import TemplateView

from web_empresa.models import Aliado, GaleriaFotoEmpresa
from web_clientes.models import Cliente


@method_decorator(gzip_page, name='dispatch')
class IndexView(TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aliados_list'] = Aliado.objects.all()
        context['clientes_list'] = Cliente.objects.all().order_by('orden')
        context['galeria_fotos_empresa_list'] = GaleriaFotoEmpresa.objects.all().order_by('orden')
        return context


class SolucionView(TemplateView):
    template_name = 'web/soluciones/solucion_detail.html'
