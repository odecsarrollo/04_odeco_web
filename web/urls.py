from django.conf.urls import url

from .views import (
    SendContactenosView
)

urlpatterns = [
    url(r'^send_contactenos/$', SendContactenosView.as_view(), name='send_contactenos'),
]
