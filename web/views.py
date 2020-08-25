from django.conf import settings

from django.core.mail import EmailMessage
from django.shortcuts import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.utils import translation
from django.views.generic import TemplateView, View

from django_redis import get_redis_connection

from odecopack.mixin import RecaptchaMixin
from web_empresa.models import Aliado, GaleriaFotoEmpresa
from web_clientes.models import Cliente, ClienteIndustria

from mailchimp3 import MailChimp


@method_decorator(gzip_page, name='dispatch')
class IndexView(TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aliados_list'] = Aliado.objects.all()
        context['industrias_list'] = ClienteIndustria.objects.prefetch_related('clientes').all().order_by('orden')
        # context['clientes_list'] = Cliente.objects.all().order_by('orden')
        context['galeria_fotos_empresa_list'] = GaleriaFotoEmpresa.objects.filter(activo=True).order_by('orden')
        return context


class TratamientoDatosPersonalesView(TemplateView):
    template_name = 'web/base/terminos_condiciones_tratamiento_datos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SolucionView(TemplateView):
    template_name = 'web/soluciones/solucion_detail.html'


class RedisListView(TemplateView):
    template_name = 'web/redis/keys_list.html'

    def get(self, request, *args, **kwargs):
        borrar_todo = self.request.GET.get('borrar_todo', None)
        if borrar_todo:
            conexion = get_redis_connection(borrar_todo)
            conexion.flushall()
        return super().get(request, *args, **kwargs)


class SendContactenosView(RecaptchaMixin, View):
    def post(self, request, *args, **kwargs):
        correo = request.POST.get('correo', None)
        nombre = request.POST.get('nombre', None)
        telefono = request.POST.get('telefono', None)
        asunto = request.POST.get('asunto', None)
        texto = request.POST.get('texto', None)
        empresa = request.POST.get('empresa', None)

        if self.revisar_recaptcha():
            mensaje = 'Asunto: %s \r\nDe: %s \r\nCorreo: %s \r\nTeléfono: %s \r\nEmpresa: %s \r\n\r\nMensaje:\r\n%s' % (
                asunto,
                nombre,
                correo,
                telefono,
                empresa,
                texto
            )

            mensaje2 = '%s:\r\n \r\n \r\nAsunto: %s \r\nDe: %s \r\nTeléfono: %s \r\nCorreo: %s \r\nEmpresa: %s \r\n\r\nMensaje: \r\n%s \r\n \r\n %s' % (
                translation.ugettext(
                    'Su mensaje con la siguiente información, para Odecopack, se ha enviado correctamente'),
                asunto,
                nombre,
                telefono,
                correo,
                empresa,
                texto,
                translation.ugettext('Pronto estaremos en contacto.')
            )

            client = MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_API_KEY)
            client.lists.members.create_or_update(settings.MAILCHIMP_LIST_ID, correo, {
                'email_address': correo,
                'status': 'subscribed',
                'status_if_new': 'subscribed',
                'merge_fields': {
                    'FNAME': nombre,
                    'COMPANY': empresa
                },
            })

            email = EmailMessage(
                subject=asunto,
                body=mensaje,
                from_email='Contactenos Odecopack SAS<webmaster@odecopack.co>',
                to=['info@odecopack.com'],
                reply_to=[correo]
            )

            email.send()

            email2 = EmailMessage(
                subject=translation.ugettext('Su envío de correo a Odecopack'),
                body=mensaje2,
                from_email='%s Odecopack SAS<webmaster@odecopack.co>' % (translation.ugettext('CONTÁCTENOS').title()),
                to=[correo]
            )
            email2.send()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
