from django.contrib import admin
from .models import Informe, Acuerdo, Participante, Objetivo, Agenda, Hallazgo, Fortaleza, Limitacion, Recomendacion, Otros

# Register your models here.
admin.site.register(Informe)
admin.site.register(Acuerdo)
admin.site.register(Participante)
admin.site.register(Objetivo)
admin.site.register(Agenda)
admin.site.register(Hallazgo)
admin.site.register(Fortaleza)
admin.site.register(Limitacion)
admin.site.register(Recomendacion)
admin.site.register(Otros)