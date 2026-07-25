from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Distrito

# Create your models here.
class Cluster(models.Model):
    numero = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"

    def __str__(self):
        return self.numero

class Monitor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"

    def __str__(self):
        return f"{self.usario.first_name} {self.usuario.last_name}"


class Escuela(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255, unique=True)
    nombre_corto = models.CharField(max_length=100, unique=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.distrito.nombre}"
    
    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"


class Director(models.Model):
    nombres = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=125)
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField(default=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.escuela.nombre_corto}"







