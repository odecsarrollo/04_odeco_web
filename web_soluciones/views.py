from django.db.models import Prefetch
from django.db.models import Q
from django.views.decorators.gzip import gzip_page
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from django.utils.translation import get_language

from .models import Documento
from .models import ItemSolucionVideo
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
        english_language = get_language() == 'en'

        if english_language:
            videos_queryset = ItemSolucionVideo.objects.filter(en_ingles=True)
            documentos_queryset = Documento.objects.filter(en_ingles=True, nombre_en__isnull=False)
        else:
            videos_queryset = ItemSolucionVideo.objects.filter(en_espanol=True)
            documentos_queryset = Documento.objects.filter(en_espanol=True, nombre__isnull=False)

        qs_mis_items = ItemSolucion.objects.filter(
            solucion__id=id,
            activo=True
        ).select_related(
            'solucion',
            'categoria_item'
        ).prefetch_related(
            'mis_imagenes',
            Prefetch('mis_documentos', queryset=documentos_queryset),
            Prefetch('mis_videos', queryset=videos_queryset)
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
