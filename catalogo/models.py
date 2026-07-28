from django.db import models


class CatalogoBase(models.Model):
    """Clase base abstracta para catálogos simples (nombre + representación en texto).

    Evita repetir el mismo patrón (CharField + Meta + __str__) en cada catálogo.
    """
    nombre = models.CharField(max_length=250, unique=True)

    class Meta:
        abstract = True
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class CatalogoParticipante(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"


class CatalogoObjetivos(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Objetivo"
        verbose_name_plural = "Objetivos"


class CatalogoAgenda(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"


class CatalogoHallazgo(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Hallazgo"
        verbose_name_plural = "Hallazgos"


class CatalogoFortaleza(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Fortaleza"
        verbose_name_plural = "Fortalezas"


class CatalogoLimitacion(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Limitación"
        verbose_name_plural = "Limitaciones"


class CatalogoRecomendacion(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Recomendación"
        verbose_name_plural = "Recomendaciones"

class CatalogoActividad(CatalogoBase):
    class Meta(CatalogoBase.Meta):
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"



class Distrito(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre