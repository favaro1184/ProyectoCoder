from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', ver_cursos),
    path('profesores/', ver_profes),
    path('entregas/', ver_entregas),
    path('estudiantes/', ver_estudiantes),
]