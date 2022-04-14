from django.views.decorators.gzip import gzip_page
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from .models import Solucion, ItemSolucion, ItemSolucionImagen


@method_decorator(gzip_page, name='dispatch')
class SolucionDetailView(DetailView):
    model = Solucion
    template_name = 'web/soluciones/solucion_detail.html'
    context_object_name = 'solucion_objeto'

    def get_object(self, queryset=None):
        slug_en = self.kwargs.get('slug_en')
        if slug_en:
            return Solucion.objects.filter(slug_en=slug_en).get()
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.object.pk
        qs_mis_items = ItemSolucion.objects.filter(
            solucion__id=id,
            activo=True
        ).select_related(
            'solucion',
            'categoria_item'
        ).prefetch_related(
            'mis_imagenes',
            'mis_documentos',
            'mis_videos'
        ).all()
        context['mis_items'] = qs_mis_items
        return context


class ItemImageSolucionDetailView(DetailView):
    model = ItemSolucionImagen
    template_name = 'web/soluciones/item_image.html'
    queryset = ItemSolucionImagen.objects.select_related('item_solucion')

    context_object_name = 'imagen'

    def get_object(self, queryset=None):
        slug_en = self.kwargs.get('slug_en')
        if slug_en:
            return queryset.filter(slug_en=slug_en).get()
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context
