from django.db import models
from organizacion.models import Escuela
from catalogo.models import CatalogoParticipante, CatalogoAgenda, CatalogoFortaleza, CatalogoHallazgo, CatalogoLimitacion, CatalogoObjetivos, CatalogoRecomendacion

# Create your models here.
class Informe(models.Model):
    actividad = models.TextField()
    fecha = models.DateField()
    esuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

class Acuerdo(models.Model):
    nombre = models.CharField(max_length=250)
    responsable = models.CharField(max_length=250)
    fecha = models.DateField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Participante(models.Model):
    tipoParticipante = models.ForeignKey(CatalogoParticipante, on_delete=models.CASCADE)
    cantidadHombre = models.IntegerField()
    cantidadMujer = models.IntegerField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Objetivo(models.Model):
    objetivo = models.ForeignKey(CatalogoObjetivos, on_delete=models.CASCADE)
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Agenda(models.Model):
    agenda = models.ForeignKey(CatalogoAgenda, on_delete=models.CASCADE)
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Hallazgo(models.Model):
    hallazgo = models.ForeignKey(CatalogoHallazgo, on_delete=models.CASCADE)
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Fortaleza(models.Model):
    fortaleza = models.ForeignKey(CatalogoFortaleza, on_delete=models.CASCADE)
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Limitacion(models.Model):
    limitacion = models.ForeignKey(CatalogoLimitacion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Recomendacion(models.Model):
    recomendacion = models.ForeignKey(CatalogoRecomendacion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)

class Otros(models.Model):
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE)