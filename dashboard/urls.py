from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboardView, name='dashboard'),
    path('escuelas-pendientes/', views.escuelasPendientesModal, name='escuelas_pendientes_modal'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]