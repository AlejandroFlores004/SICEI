from django.contrib import admin

from catalogo.models import CatalogoAgenda, CatalogoFortaleza, CatalogoHallazgo, CatalogoLimitacion, CatalogoObjetivos, CatalogoParticipante

# Register your models here.
admin.site.register(CatalogoParticipante)
admin.site.register(CatalogoObjetivos)
admin.site.register(CatalogoAgenda)
admin.site.register(CatalogoHallazgo)
admin.site.register(CatalogoFortaleza)
admin.site.register(CatalogoLimitacion)