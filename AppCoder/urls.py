from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', ver_cursos, name="VerCursos"),
    path('profesores/', ver_profes, name="VerProfes"),
    path('entregas/', ver_entregas, name="VerEntregas"),
    path('estudiantes/', ver_estudiantes, name="VerEstudiantes"),
]