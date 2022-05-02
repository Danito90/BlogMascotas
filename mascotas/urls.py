from django.contrib import admin
from django.urls import path
from mascotas.views import *

urlpatterns = [
    path('agregarMascota/', agregarMascota, name='agregarMascota'),
    path('detalleMascota/<int:id>/', detalleMascota, name='detalleMascota'),
    path('actualizarMascota/<int:id>/', actualizarMascota, name='actualizarMascota'),
    path('eliminarMascota/<int:id>/', eliminarMascota, name='eliminarMascota'),
]