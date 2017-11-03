from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from .models import ClienteContacto


class RecoleccionContactoView(CreateView):
    model = ClienteContacto
    fields = '__all__'
    template_name = 'web/formulario_recoleccion_contactos.html'

    def get_success_url(self):
        return reverse('contactos:recoleccion_contacto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contactos_recolectado'] = ClienteContacto.objects.all().order_by('-id')[0:10]
        return context
