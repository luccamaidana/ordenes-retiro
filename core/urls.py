from django.urls import path
from . import views

urlpatterns = [
    path('orden/nueva/', views.crear_orden_pedido, name='crear_orden_pedido'),
]