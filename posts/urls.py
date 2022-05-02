from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('agregarPost/', agregarPost, name='agregarPost'),
    path('detallePost/<int:id>/', detallePost, name='detallePost'),
    path('actualizarPost/<int:id>/', actualizarPost, name='actualizarPost'),
    path('eliminarPost/<int:id>/', eliminarPost, name='eliminarPost'),
]