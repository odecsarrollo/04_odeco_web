from django.shortcuts import render
from django.views.generic.list import ListView

from .models import CasoExito


class CasosExitoListView(ListView):
    model = CasoExito
    template_name = 'web/casos_exito/casos_exito_list.html'
    queryset = CasoExito.objects.filter(
        activo=True
    ).select_related(
        'industria',
        'cliente'
    ).prefetch_related(
        'mis_testimonios',
        'mis_imagenes',
        'mis_videos'
    ).all()
    context_object_name = 'casos_exito_lista'
