from django.urls import path
from .views import CasosExitoListView

urlpatterns = [
    path('lista/', CasosExitoListView.as_view(), name='lista')
]
