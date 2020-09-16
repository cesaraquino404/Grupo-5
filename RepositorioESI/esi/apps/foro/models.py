from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify

class Tematica(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre



class Tematica(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    tematica = models.ForeignKey(Tematica, related_name='miTematica', null=True, on_delete=models.SET_NULL)
<<<<<<< HEAD
    
=======

>>>>>>> b439f0d7cf25c5b0a8664f221b380903c82c516c
    def __str__(self):
        return self.titulo
