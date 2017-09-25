from django.conf.urls import url
from django.contrib import admin

from web.views import IndexView, SolucionView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^solucion$', SolucionView.as_view(), name='solucion'),
]
