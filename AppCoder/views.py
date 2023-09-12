from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor
from AppCoder.models import Curso
"""""
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
    return HttpResponse("Pagina de Inicio")

def ver_cursos(request):
    return HttpResponse("Pagina de Cursos")

def ver_profes(request):
    return HttpResponse("Pagina de Profesores")

def ver_entregas(request):
    return HttpResponse("Pagina de Entregas")

def ver_estudiantes(request):
    return HttpResponse("Pagina de Estudiantes")

