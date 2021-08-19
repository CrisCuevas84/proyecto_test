from django.urls import path, include
from . import views


# Todas las rutas de la app cliente están incluidas acá
urlpatterns = [
    # '' me redirige al views, al método o función cliente
    path('', views.inicio), # Acceso por defecto
    # path('/inicio', views.inicio), error concatenacion rutas cliente//inicio
    path('inicio', views.inicio),
    # CRUD
    path('agregar', views.agregar), # Create - Crear
    path('leer', views.leer), # Read - Leer
    path('actualizar', views.actualizar), # Update - Actualizar
    path('eliminar', views.eliminar), # Delete - Eliminar
]