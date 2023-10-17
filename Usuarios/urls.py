from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('registro', views.registro),
    path('index', views.index, name='index'),
    path('cerrar-sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('recuperar_pass', views.recuperar_pass, name='recuperar_pass'),
    path('buscar_materia', views.buscarMateria, name='buscarMateria'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('perfil', views.perfil, name='perfil')
   # path('crear_grupo', views.)
]