from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from web.views import IndexView, RedisListView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^redis/', RedisListView.as_view(), name='redis'),
    url(r'^soluciones/', include('web_soluciones.urls', namespace='web_soluciones')),
    url(r'^casos_exito/', include('web_casos_exito.urls', namespace='web_casos_exito')),
    url(r'^web/', include('web.urls', namespace='web')),
    url(r'^feria/', include('web_contactos.urls', namespace='contactos')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
