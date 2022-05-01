from django import forms
from django.forms import ModelForm

from mascotas.models import Mascota


class mascotaForm(ModelForm, forms.Form):

    class Meta:
        model = Mascota
        fields = [
            'id_autor', 'tipo', 'nombreMascota', 'razaPerro', 'razaGato',
            'edad', 'tamano', 'color', 'collar', 'genero', 'foto', 'activo', 'codigo']
        labels = {
            'id_autor': 'Dueño',
            'tipo': 'Tipo',
            'nombreMascota': 'Nombre',
            'razaPerro': 'Raza',
            'razaGato': 'Raza',
            'edad': 'Edad',
            'tamano': 'Tamaño',
            'color': 'Color',
            'collar': 'Collar',
            'genero': 'Genero',
            'foto': 'Foto',
            'codigo': 'Codigo',
            'activo': 'Activo',
            }
        help_texts = {
            'id_autor': 'Ingrese su dueño',
            'tipo': 'Ingrese el tipo de mascota',
            'nombreMascota': 'Ingrese el Nombre de la mascota',
            'razaPerro': 'Ingrese la raza de la mascota',
            'razaGato': 'Ingrese la raza de la mascota',
            'edad': 'Ingrese la edad de la mascota',
            'tamano': 'Ingrese el tamaño de la mascota',
            'color': 'Ingrese el color de la mascota',
            'collar': 'Ingrese si tiene collar',
            'genero': 'Ingrese el genero de la mascota',
            'foto': 'Ingrese la foto de la mascota',
            'codigo': 'Ingrese el codigo de la mascota',
            'activo': 'Ingrese si la mascota esta activa',
                      }
        error_messages = {
            'id_autor': {'max_length': "Este campo no puede tener mas de 20 caracteres"},
            'tipo': {'max_length': "Este campo no puede tener mas de 50 caracteres"},
            'nombreMascota': {'max_length': "Este campo no puede tener mas de 80 caracteres"},
            'codigo': {'max_length': "Este campo no puede tener mas de 50 caracteres"},
            }
        widgets = {
            'id_autor': forms.TextInput(attrs={'placeholder': 'Ingrese su dueño'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ingrese el tipo de mascota'}),
            'color': forms.TextInput(attrs={'type': 'color', 'placeholder': 'Ingrese el color de la mascota'}),
            }

    # Modificar el método de inicialización de la clase para lograr el propósito de agregar atributos comunes en lote
    def __init__(self, *args, **kwargs):
        super(Mascota, self).__init__(*args, **kwargs)
        # for field_name in self.base_fields:
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})


