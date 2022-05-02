from django.db import models
from autores.models import Autor
from mascotas.choices import EDAD, GENERO, TAMANO, RAZAGATOS, RAZAPERROS


class Mascota(models.Model):
    id_autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=[(
        'Perro', 'Perro'), ('Gato', 'Gato'), ], default='Perro')
    nombreMascota = models.CharField(max_length=80)
    razaPerro = models.CharField(
        max_length=80, choices=RAZAPERROS, default='Seleccionar')
    razaGato = models.CharField(
        choices=RAZAGATOS, default='Seleccionar', max_length=80)
    edad = models.CharField(choices=EDAD, default='Joven', max_length=50)
    tamano = models.CharField(choices=TAMANO, default='Pequeño', max_length=50)
    color = models.CharField(max_length=200, null=True, blank=True)
    collar = models.BooleanField(default=False)
    genero = models.CharField(choices=GENERO, default='Macho', max_length=50)
    foto = models.ImageField(
        upload_to='mascotas', null=True, blank=True)
    codigo = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombreMascota", "edad"]
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        # unique_together = (('banco', 'numCh',),) # par de campos unicos en tupla
        constraints = [
            models.UniqueConstraint(
                fields=['id_autor', 'nombreMascota', 'edad'], name='Mascota unica')
        ]  # tambien para campos unicos en pares

    def __str__(self):
        return f"{self.id_autor} - {self.nombreMascota}: {self.razaPerro}, {self.razaGato}, {self.edad}, {self.tamaño}, {self.color}, {self.collar}, {self.genero}, {self.foto}, {self.activo}"
