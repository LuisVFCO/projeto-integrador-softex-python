from django.urls import path
from . import views

urlpatterns = [
    path('ver_buscador/', views.ver_buscador_noticias, name="ver_buscador_noticias")
]