from django.contrib import admin
from django.urls import path
from autores.views import *

urlpatterns = [
    path('agregarAutor/', agregarAutor, name='agregarAutor'),
    path('detalleAutor/<int:id>/', detalleAutor, name='detalleAutor'),
    path('actualizarAutor/<int:id>/', actualizarAutor, name='actualizarAutor'),
    path('eliminarAutor/<int:id>/', eliminarAutor, name='eliminarAutor'),
]