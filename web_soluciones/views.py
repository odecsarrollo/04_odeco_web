from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Solucion


class SolucionDetailView(DetailView):
    model = Solucion
    template_name = 'web/soluciones/solucion_detail.html'
    context_object_name = 'solucion_objeto'
