from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor
from AppCoder.models import Curso
"""
def profe_nuevo(request):
    profeN = Profesor(nombre="pepe", apellido="gonzalez", email="pepe@gmail.com", profesion="matematico")
    profeN.save()
    
    return HttpResponse(f"Se a creado un profesor nuevo {profeN.nombre}")

def curso_nuevo(request):
    cursoN = Curso(nombre="Python", comision=47765)
    cursoN.save()
    
    return HttpResponse(f"Se a creado un Curso nuevo {cursoN.nombre}")
"""
def inicio(request):
    nombre = 'fabian'
    return render(request, "AppCoder/inicio.html",{"name":nombre})

def ver_cursos(request):
    return render(request, "AppCoder/ver_cursos.html")

def ver_profes(request):
    return render(request, "AppCoder/ver_profes.html")

def ver_entregas(request):
    return render(request, "AppCoder/ver_entregas.html")

def ver_estudiantes(request):
    return render(request, "AppCoder/ver_estudiantes.html")

