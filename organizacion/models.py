from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Distrito


class Cluster(models.Model):
    numero = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"
        ordering = ['numero']

    def __str__(self):
        return self.numero


class Monitor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='monitor')
    telefono = models.CharField(max_length=8)

    zonas = [
        ('S','SUR'),
        ('N','NORTE'),
    ]
    zona = models.CharField(max_length=2, choices=zonas, default = 'S')

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"

    def __str__(self):
        # Fixed typo: was self.usario (would raise AttributeError)
        nombre_completo = f"{self.usuario.first_name} {self.usuario.last_name}".strip()
        return nombre_completo or self.usuario.username


class Escuela(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255, unique=True)
    nombre_corto = models.CharField(max_length=100, unique=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name='escuelas')
    estado = models.BooleanField(default=True)
    monitor = models.ForeignKey(
        Monitor, on_delete=models.SET_NULL, null=True, blank=True, related_name='escuelas'
    )

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.distrito.nombre}"


class Director(models.Model):
    nombres = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=125)
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField(default=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='directores')

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.escuela.nombre_corto}"