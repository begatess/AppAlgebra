from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login),
    path('materias', views.listar_materias),
    path('dashboard/<int:nrc>/', views.dashboard, name='dashboard'),
    path('materias_prueba', views.listar_materias_profesor, name='materias_prueba'),
    path('crear-grupo', views.crearGrupo, name='crear-grupo')
    #path('dashboard', views.dashboard)
]