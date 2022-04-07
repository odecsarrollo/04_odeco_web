from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from web.views import IndexView, RedisListView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('redis/', RedisListView.as_view(), name='redis'),
    path('soluciones/', include(('web_soluciones.urls', 'web_soluciones'), namespace='web_soluciones')),
    path('casos_exito/', include(('web_casos_exito.urls', 'web_casos_exito'), namespace='web_casos_exito')),
    path('web/', include(('web.urls', 'web'), namespace='web')),
    path('feria/', include(('web_contactos.urls', 'web_contactos'), namespace='contactos')),
    path('tinymce/', include('tinymce.urls')),
    path('rosetta/', include('rosetta.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
