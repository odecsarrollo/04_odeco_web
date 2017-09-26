from django.conf.urls import url
from .views import SolucionDetailView

urlpatterns = [
    url(r'^solucion/(?P<pk>[0-9]+)/$', SolucionDetailView.as_view(), name='solucion_detail'),
    url(r'^solucion/(?P<slug>[0-9A-Za-z-]+)/$', SolucionDetailView.as_view(), name='solucion_detail_slug'),
]
