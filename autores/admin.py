from django.contrib import admin
from autores.models import Autor

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','id_contacto','domicilio','nacimiento','foto','activo','created')  # modo tabla en admin
    search_fields = ('nombre','apellido','id_contacto','activo')  # barra de busqueda
    list_filter = ('nombre','apellido','id_contacto','activo')  # filtros a la derecha
    ordering = ('nombre','apellido','id_contacto',) # orden descendiente , para orden ascendiente: '-fechaVto'

admin.site.register(Autor,AutorAdmin)