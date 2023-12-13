from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
   path("", views.tiendas, name='tiendas'),
   path("productos", views.productos, name='productos'),
   path("tiendas", views.tiendas, name='tiendas'),
   path("detTiendas/<int:tienda_id>/", views.detTiendas, name='detTiendas'),
   path("ingresoTiendas", views.ingresoTiendas, name='ingresoTiendas'),
   path("eliminarTienda/<int:tienda_id>/", views.eliminarTienda, name='eliminarTienda'),
   path("ingresoProductos", views.ingresoProductos, name='ingresoProductos'),
   path("eliminarProducto/<int:producto_id>/", views.eliminarProducto, name='eliminarProducto')
]