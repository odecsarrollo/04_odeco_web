from django.conf.urls import url
from .views import CasosExitoListView

urlpatterns = [
    url(r'^lista/$', CasosExitoListView.as_view(), name='lista')
    # url(r'^solucion/(?P<pk>[0-9]+)/$', SolucionDetailView.as_view(), name='solucion_detail'),
]
