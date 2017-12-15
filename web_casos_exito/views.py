from django.shortcuts import render
from django.views.generic.list import ListView

from .models import CasoExito


class CasosExitoListView(ListView):
    model = CasoExito
    template_name = 'web/casos_exito/casos_exito_list.html'
    queryset = CasoExito.objects.select_related('industria', 'cliente').all()
    context_object_name = 'casos_exito_lista'
