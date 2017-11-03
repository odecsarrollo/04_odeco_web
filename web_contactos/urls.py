from django.conf.urls import url
from .views import RecoleccionContactoView

urlpatterns = [
    url(r'^$', RecoleccionContactoView.as_view(), name='recoleccion_contacto'),
]
