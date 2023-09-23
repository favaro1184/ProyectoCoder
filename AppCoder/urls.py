from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),

    #urls de leer
    path('cursos/', ver_cursos, name="VerCursos"),
    path('profesores/', ver_profes, name="VerProfes"),
    path('entregas/', ver_entregas, name="VerEntregas"),
    path('estudiantes/', ver_estudiantes, name="VerEstudiantes"),
    
    #urls de crear
    path('crearCurso/', crear_cursos, name="CrearCursos"),
    path('crearProfesor/', crear_profes, name="CrearProfesor"),
    
    #urls de busqueda
    path('buscarProfesor/', buscar_profes, name="BuscarProfesor"),
    path('resultadoProfesor/', resultado_profes, name="ResultadoProfesor"),
    
     #urls de borrado
     path('eliminarProfesor/<profesor_nombre>', eliminar_profes, name="EliminarProfesor"),
]