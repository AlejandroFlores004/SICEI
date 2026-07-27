from django.contrib import admin
from .models import Cluster, Director, Monitor, Escuela


class DirectorInline(admin.TabularInline):
    model = Director
    extra = 1
    fields = ('nombres', 'apellidos', 'telefono', 'estado')


@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_corto', 'distrito', 'monitor', 'estado')
    list_filter = ('distrito', 'estado')
    search_fields = ('codigo', 'nombre', 'nombre_corto')
    inlines = [DirectorInline]  # crea el/los director(es) al mismo tiempo que la escuela


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'telefono', 'escuela', 'estado')
    list_filter = ('estado', 'escuela__distrito')
    search_fields = ('nombres', 'apellidos')


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'usuario__username')


admin.site.register(Cluster)