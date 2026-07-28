from django.contrib import admin

from .models import (
    CatalogoParticipante,
    CatalogoObjetivos,
    CatalogoAgenda,
    CatalogoHallazgo,
    CatalogoFortaleza,
    CatalogoLimitacion,
    CatalogoRecomendacion,
    CatalogoActividad,
    Distrito,
)


@admin.register(
    CatalogoParticipante,
    CatalogoObjetivos,
    CatalogoAgenda,
    CatalogoHallazgo,
    CatalogoFortaleza,
    CatalogoLimitacion,
    CatalogoRecomendacion,
    CatalogoActividad,
    Distrito,
)
class CatalogoAdmin(admin.ModelAdmin):
    """Un solo ModelAdmin reutilizado para todos los catálogos simples."""
    list_display = ('nombre',)
    search_fields = ('nombre',)