from django.contrib.sitemaps import Sitemap

from web_soluciones.models import ItemSolucionImagen, Solucion

from web_configurations.models import CacheConfiguration


class SolutionsSitemap(Sitemap):
    def items(self):
        return Solucion.objects.order_by('id').all()

    def lastmod(self, obj):
        return CacheConfiguration.objects.first().soluciones_update


class ItemSolutionsSitemap(Sitemap):
    def items(self):
        return ItemSolucionImagen.objects.order_by('id').all()

    def lastmod(self, obj):
        return obj.modified or obj.created
