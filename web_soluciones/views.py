from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Solucion, ItemSolucion


class SolucionDetailView(DetailView):
    model = Solucion
    template_name = 'web/soluciones/solucion_detail.html'
    context_object_name = 'solucion_objeto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mis_items'] = self.object.mis_items.prefetch_related('mis_imagenes').all()
        #ItemSolucion.objects.prefetch_related('mis_imagenes')
        return context
