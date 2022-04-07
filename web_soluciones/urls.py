from django.urls import path

from .views import ItemImageSolucionDetailView, SolucionDetailView

urlpatterns = [
    path('solucion/<int:pk>', SolucionDetailView.as_view(), name='solucion_detail'),
    path('solucion/<slug:slug>', SolucionDetailView.as_view(), name='solucion_detail_slug'),
    path('imagen/<int:pk>', ItemImageSolucionDetailView.as_view(), name='item_solucion_image'),
]
