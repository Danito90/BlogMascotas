


from django import forms
from django.forms import ModelForm

from autores.models import Autor


class autorForm(ModelForm,forms.Form):
    
    class Meta:
        model=Autor
        fields= ['nombre','apellido','id_contacto','domicilio','nacimiento','foto','activo']
        widgets = {
            "nacimiento": forms.widgets.DateInput(
                                 # Agregar tipo de fecha al campo de fecha
                attrs={"type": "date"}
            )
        }
        
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido', 
            'id_contacto':'Contacto',
            'domicilio':'Domicilio',
            'domicilio':'Domicilio',
            'nacimiento':'Nacimiento',
            'foto':'Foto',
            'activo':'Activo',
        }
