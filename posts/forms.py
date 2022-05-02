from autores.models import Autor
from mascotas.models import Mascota
from posts.models import Post

from django import forms
from django.forms import ModelForm


class postForm(ModelForm, forms.Form):
    id_autor = forms.ModelChoiceField(
        label='Autor', required=True, queryset=Autor.objects.all(), empty_label="Seleccione el Autor")
    id_mascota = forms.ModelChoiceField(
        label='Mascota', required=True, queryset=Mascota.objects.all(), empty_label="Seleccione la mascota")

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['created', 'updated', 'visto']
        labels = {
            'id_autor': 'Autor',
            'titulo': 'Titulo',
            'subTitulo': 'Subtitulo',
            'id_mascota': 'Mascota',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
            'ubicacion': 'Ubicacion',
            'fecha': 'Fecha',
            'foto': 'Foto',
            'reencuentro': 'Reencuentro',
            'activo': 'Activo',
        }
        error_messages = {


        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'style': 'width:500px; height:200px', 'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
        }
