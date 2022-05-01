from django.db import models

from contactos.models import Contacto

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    id_contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, blank=True, null=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    foto= models.ImageField(upload_to='autores/images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    
    class Meta:
        ordering = ["nombre", "apellido"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        #unique_together = (('banco', 'numCh',),) # par de campos unicos en tupla
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'apellido','nacimiento'], name='Autor unico')
        ] # tambien para campos unicos en pares
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}: {self.nacimiento}, {self.foto}, {self.activo}"