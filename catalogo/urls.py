from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_home, name='catalogo_home'),
    path('panel/<slug:catalogo>/', views.catalogo_panel, name='catalogo_panel'),
    path('<slug:catalogo>/nuevo/', views.catalogo_create, name='catalogo_create'),
]