from django.urls import path
from . import views

urlpatterns = [
    path('', views.informe_list, name='actividad_home'),
    path('nuevo/', views.informe_form, name='informe_create'),
    path('<int:pk>/editar/', views.informe_form, name='informe_update'),
    path('<int:pk>/ver/', views.informe_detalle, name='informe_detalle'),
    path('<int:pk>/eliminar/', views.informe_delete, name='informe_delete'),
]
