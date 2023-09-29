from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

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
     path('eliminarProfesor/<profesor_id>', eliminar_profes, name="EliminarProfesor"),
     
     #urls de actualizado
     path('actualizarProfesor/<profesor_id>', actualizar_profes, name="ActualizarProfesor"),
     
     #####################################################
     #crud usando vistas
     path('estudiantes/lista/', EstudianteLista.as_view(), name="VerEstudiantesLista"),
     path('estudiantes/nuevo/', EstudianteCrear.as_view(), name="CrearEstudiantes"),
     path('estudiantes/actualizar/<int:pk>', EstudianteActualizar.as_view(), name="ActualizarEstudiantes"),
     path('estudiantes/borrar/<int:pk>', EstudianteBorrar.as_view(), name="BorrarEstudiantes"),
     path('estudiantes/detalle/<int:pk>', EstudianteDetalle.as_view(), name="DetalleEstudiantes"),
     
     path('login/', login_view, name="InicioSesion"),
     path('register/', register, name="RegistroUsuarios"),
     path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),

]