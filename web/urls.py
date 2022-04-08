from django.contrib import admin
from django.urls import path

from .views import (
    SendContactenosView,
    TratamientoDatosPersonalesView
)

admin.site.site_header = 'Administración Página de Odecopack'

urlpatterns = [
    path('send_contactenos/', SendContactenosView.as_view(), name='send_contactenos'),
    path('tratamiento_datos_personales/', TratamientoDatosPersonalesView.as_view(),
         name='tratamiento_datos_personales'),
]
