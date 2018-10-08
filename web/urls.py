from django.conf.urls import url

from .views import (
    SendContactenosView,
    TratamientoDatosPersonalesView
)

urlpatterns = [
    url(r'^send_contactenos/$', SendContactenosView.as_view(), name='send_contactenos'),
    url(r'^tratamiento_datos_personales/$', TratamientoDatosPersonalesView.as_view(), name='tratamiento_datos_personales'),
]
