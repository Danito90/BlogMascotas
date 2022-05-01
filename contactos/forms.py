from django.forms import CharField, EmailField, IntegerField, ModelForm
from django import forms

from contactos.models import Contacto


class contactoForm(ModelForm, forms.Form):
    # celular= IntegerField()
    # whatsapp = IntegerField()
    # mail = EmailField()
    
    class Meta:
        model = Contacto
        fields = ['celular', 'whatsapp', 'mail']
        labels = {
            'celular': 'Celular',
            'whatsapp': 'Whatsapp',
            'mail': 'Mail',
        }
        help_texts = {
            'celular': 'Ingrese su celular',
            'whatsapp': 'Ingrese su whatsapp',
            'mail': 'Ingrese su mail',
        }
        error_messages = {
            'celular': {
                'max_length': "Este campo no puede tener mas de 20 caracteres",
            },
            'whatsapp': {
                'max_length': "Este campo no puede tener mas de 20 caracteres",
            },
            'mail': {
                'max_length': "Este campo no puede tener mas de 80 caracteres",
            },
        }
        widgets = {
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su celular'}),
            'whatsapp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su whatsapp'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mail'}),
        }


