from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.views.generic import TemplateView, View

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


class SendContactenosView(View):
    def post(self, request, *args, **kwargs):
        # form = MensajeContactoForm(self.request.POST)
        #
        # if form.is_valid():
        #     form.save()
        #
        #     instancia_contactenos = form.instance
        #
        #     mensaje = 'Mensaje Id: %s \r\n Asunto: %s \r\n De: %s \r\n Correo: %s \r\n Celular: %s \r\n \r\n Mensaje: \r\n \r\n %s' % (
        #         instancia_contactenos.id,
        #         instancia_contactenos.asunto_contacto.nombre,
        #         instancia_contactenos.nombres,
        #         instancia_contactenos.email,
        #         instancia_contactenos.celular,
        #         instancia_contactenos.mensaje
        #     )
        #
        #     email = EmailMessage(
        #         subject=instancia_contactenos.asunto_contacto.nombre,
        #         body=mensaje,
        #         from_email='Contactenos Dr. Amor<contactenos@clinicadramor.com>',
        #         to=['contactenos@clinicadramor.com'],
        #         reply_to=[instancia_contactenos.email],
        #         headers={'Message-ID': instancia_contactenos.id}
        #     )
        #
        #     email.send()
        #
        #     messages.info(self.request, "Su mensaje fué enviado correctamente")

        return redirect('index')
