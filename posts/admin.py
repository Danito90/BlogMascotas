from django.contrib import admin

from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id_autor','id_mascota','descripcion','titulo','subTitulo','estado','ubicacion','fecha','foto','visto','reencuentro','activo','created','updated')  # modo tabla en admin
    search_fields = ('id_autor','id_mascota','titulo','estado','ubicacion','fecha','foto',)  # barra de busqueda
    list_filter = ('id_autor','id_mascota','estado','ubicacion','fecha','foto','reencuentro','activo',)  # filtros a la derecha
    ordering = ('fecha','titulo') # orden descendiente , para orden ascendiente: '-fechaVto'

admin.site.register(Post, PostAdmin)
