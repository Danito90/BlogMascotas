from django.db import models


class Contacto(models.Model):
    celular = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    mail = models.CharField(max_length=80, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["mail"]
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"


    def __str__(self):
        return f"{self.celular}: {self.whatsapp}, {self.mail}"
