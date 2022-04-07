from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from web_configurations.models import CacheConfiguration


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index']

    def lastmod(self, obj):
        config = CacheConfiguration.objects.first()
        return config.empresa_update or config.clientes_update

    def location(self, item):
        return reverse(item)
