from django.contrib import admin
from mascotas.models import Mascota

class MascotaAdmin(admin.ModelAdmin):
    list_fields=('id','id_autor','tipo','nombreMascota','razaPerro','razaGato','edad','tamano','color','collar','genero','foto','activo','codigo','created','updated',)
    list_filter=('id_autor','tipo','nombreMascota','razaPerro','razaGato','edad','tamano','color','collar','genero','activo',)
    search_fields= ('id_autor','tipo','nombreMascota','razaPerro','razaGato','edad','tamano','color','collar','genero','activo',)
    ordering= ('nombreMascota','tipo',)
    
admin.site.register(Mascota,MascotaAdmin)




