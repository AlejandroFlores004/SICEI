from django.db import models
from organizacion.models import Escuela
from catalogo.models import (
    CatalogoParticipante,
    CatalogoAgenda,
    CatalogoFortaleza,
    CatalogoHallazgo,
    CatalogoLimitacion,
    CatalogoObjetivos,
    CatalogoRecomendacion,
    CatalogoActividad
)


class Informe(models.Model):
    fecha = models.DateField()
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='informes')

    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.escuela.nombre_corto} - {self.fecha}"


class Acuerdo(models.Model):
    nombre = models.CharField(max_length=250)
    responsable = models.CharField(max_length=250)
    fecha = models.DateField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='acuerdos')

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    tipoParticipante = models.ForeignKey(
        CatalogoParticipante, on_delete=models.CASCADE, related_name='participantes'
    )
    cantidadHombre = models.PositiveIntegerField(default=0)
    cantidadMujer = models.PositiveIntegerField(default=0)
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.tipoParticipante} (H:{self.cantidadHombre} / M:{self.cantidadMujer})"


class Objetivo(models.Model):
    objetivo = models.ForeignKey(CatalogoObjetivos, on_delete=models.CASCADE, related_name='objetivos')
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='objetivos')

    def __str__(self):
        return str(self.objetivo)


class Actividad(models.Model):
    actividad = models.ForeignKey(CatalogoActividad, on_delete=models.CASCADE, related_name='actividades')
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='actividades')
    
    def __str__(self):
        return str(self.actividad)

class Agenda(models.Model):
    agenda = models.ForeignKey(CatalogoAgenda, on_delete=models.CASCADE, related_name='agendas')
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='agendas')

    def __str__(self):
        return str(self.agenda)


class Hallazgo(models.Model):
    hallazgo = models.ForeignKey(CatalogoHallazgo, on_delete=models.CASCADE, related_name='hallazgos')
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='hallazgos')

    def __str__(self):
        return str(self.hallazgo)


class Fortaleza(models.Model):
    fortaleza = models.ForeignKey(CatalogoFortaleza, on_delete=models.CASCADE, related_name='fortalezas')
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='fortalezas')

    def __str__(self):
        return str(self.fortaleza)


class Limitacion(models.Model):
    limitacion = models.ForeignKey(CatalogoLimitacion, on_delete=models.CASCADE, related_name='limitaciones')
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='limitaciones')

    def __str__(self):
        return str(self.limitacion)


class Recomendacion(models.Model):
    recomendacion = models.ForeignKey(
        CatalogoRecomendacion, on_delete=models.CASCADE, related_name='recomendaciones'
    )
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='recomendaciones')

    def __str__(self):
        return str(self.recomendacion)


class Otros(models.Model):
    descripcion = models.TextField()
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, related_name='otros')

    def __str__(self):
        return self.descripcion[:50]