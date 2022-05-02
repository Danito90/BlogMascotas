from django.contrib import admin
from django.urls import path
from contactos.views import *

urlpatterns = [
    path('detalleContacto', detalleContacto, name='detalleContacto'),
    path('agregarContacto/<int:id>/', agregarContacto, name='agregarContacto'),
    path('actualizarContacto/<int:id>/', actualizarContacto, name='actualizarContacto'),
    path('eliminarContacto/<int:id>/', eliminarContacto, name='eliminarContacto'),
]