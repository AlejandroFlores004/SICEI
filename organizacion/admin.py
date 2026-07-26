from django.contrib import admin
from .models import Cluster, Director, Monitor, Escuela
# Register your models here.

admin.site.register(Cluster)
admin.site.register(Director)
admin.site.register(Monitor)
admin.site.register(Escuela)