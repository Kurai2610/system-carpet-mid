from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='productos'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/',
         views.detalle_producto, name='detalle_producto'),
]
