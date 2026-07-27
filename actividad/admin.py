from django.contrib import admin
from .models import (
    Informe,
    Acuerdo,
    Participante,
    Objetivo,
    Agenda,
    Hallazgo,
    Fortaleza,
    Limitacion,
    Recomendacion,
    Otros,
)


class AgendaInline(admin.TabularInline):
    model = Agenda
    extra = 1


class ParticipanteInline(admin.TabularInline):
    model = Participante
    extra = 1


class ObjetivoInline(admin.TabularInline):
    model = Objetivo
    extra = 1


class AcuerdoInline(admin.TabularInline):
    model = Acuerdo
    extra = 1


class HallazgoInline(admin.TabularInline):
    model = Hallazgo
    extra = 1


class FortalezaInline(admin.TabularInline):
    model = Fortaleza
    extra = 1


class LimitacionInline(admin.TabularInline):
    model = Limitacion
    extra = 1


class RecomendacionInline(admin.TabularInline):
    model = Recomendacion
    extra = 1


class OtrosInline(admin.TabularInline):
    model = Otros
    extra = 1


@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    list_display = ('escuela', 'actividad', 'fecha')
    list_filter = ('escuela__distrito', 'fecha')
    search_fields = ('actividad', 'escuela__nombre', 'escuela__nombre_corto')
    date_hierarchy = 'fecha'
    # Todo lo relacionado a un Informe se crea/edita en la misma pantalla
    inlines = [
        AgendaInline,
        ParticipanteInline,
        ObjetivoInline,
        AcuerdoInline,
        HallazgoInline,
        FortalezaInline,
        LimitacionInline,
        RecomendacionInline,
        OtrosInline,
    ]