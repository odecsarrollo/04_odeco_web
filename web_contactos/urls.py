from django.urls import path

from .views import RecoleccionContactoView

urlpatterns = [
    path('', RecoleccionContactoView.as_view(), name='recoleccion_contacto'),
]
