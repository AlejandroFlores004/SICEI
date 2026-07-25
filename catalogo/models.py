from django.db import models

# Create your models here.
class CatalogoParticipante(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"

    def __str__(self):
        return self.nombre

class CatalogoObjetivos(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Objetivo"
        verbose_name_plural = "Objetivos"

    def __str__(self):
        return self.nombre

class CatalogoAgenda(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    def __str__(self):
        return self.nombre

class CatalogoHallazgo(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Hallazgo"
        verbose_name_plural = "Hallazgos"

    def __str__(self):
        return self.nombre

class CatalogoFortaleza(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Fortaleza"
        verbose_name_plural = "Fortalezas"

    def __str__(self):
        return self.nombre

class CatalogoLimitacion(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Limitación"
        verbose_name_plural = "Limitaciones"

    def __str__(self):
        return self.nombre

class CatalogoRecomendacion(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Recomendación"
        verbose_name_plural = "Recomendaciones"

    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"

