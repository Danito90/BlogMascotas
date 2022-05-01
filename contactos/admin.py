from django.contrib import admin
from contactos.models import Contacto
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display= ('celular','whatsapp','mail','created','updated','activo',)  # modo tabla en admin
    search_fields= ('celular','whatsapp','mail','activo',)
    list_filter= ('celular','whatsapp','mail','activo',)
    ordering= ('mail',)
    
admin.site.register(Contacto, ContactoAdmin)    
    