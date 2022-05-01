from django.db import models
from autores.models import Autor
from mascotas.models import Mascota
from posts.choices import ESTADO

class Post(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    subTitulo = models.CharField(max_length=100, blank=True, null=True)
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    descripcion= models.TextField()
    estado= models.CharField(choices=ESTADO,default='Buscado',max_length=50)
    ubicacion= models.CharField(max_length=200)
    fecha= models.DateTimeField(auto_now_add=True)
    visto= models.IntegerField(blank=True, null=True)
    reencuentro= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo= models.BooleanField(default=True)
       
   
    class Meta:
        ordering = ["fecha", "titulo"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        #unique_together = (('banco', 'numCh',),) # par de campos unicos en tupla
        constraints = [
            models.UniqueConstraint(fields=['id_autor', 'id_mascota','estado'], name='Post unico')
        ] # tambien para campos unicos en pares
    
    def __str__(self):
        return f"{self.autor}: {self.nombreMascota}, {self.raza}, {self.edad}, {self.estado}, {self.ubicacion}"