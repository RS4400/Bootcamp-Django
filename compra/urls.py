from django.urls import path
from . import views


urlpatterns = [
    path('list_proveedores/', views.list_proveedores, name='list-proveedores'),
    path('create_proveedor/', views.create_proveedor, name='create-proveedor'),
    path('list_productos/', views.list_productos, name='list-productos'),
    path('create_producto/', views.create_producto, name='create-producto'),
]