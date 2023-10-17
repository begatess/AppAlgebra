from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login),
    path('materias', views.listar_materias),
    path('dashboard/<int:nrc>/', views.dashboard, name='dashboard'),
    path('materias_prueba', views.listar_materias_profesor, name='materias_prueba'),
    path('crear-grupo', views.crearGrupo, name='crear-grupo'),
    path('mis_materias', views.mis_materias, name='mis_materias'),
    path('buscar_materias', views.listar_materias, name="buscar_materias"),
    path('detalles_materia/<int:nrc>/', views.detalles_materia, name="detalles_materia"),
    path('inscripcion_materia/<int:nrc>/', views.inscripcion_materia, name="inscripcion_materia")
    #path('dashboard', views.dashboard)
]