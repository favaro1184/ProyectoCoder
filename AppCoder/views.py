from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor
from AppCoder.models import Curso
from AppCoder.forms import ProfesorFormulario
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



def ver_entregas(request):
    return render(request, "AppCoder/ver_entregas.html")

def ver_estudiantes(request):
    return render(request, "AppCoder/ver_estudiantes.html")







############################################################################################################################################
#CRUD DE PROFESORES  --- CLASICO

#READ ALL  -- Cargar todos los cursos en la pagina principal de CURSOS
def ver_profes(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/ver_profes.html", {"res":profesores})

#CREATE
def crear_profes(request):
      if request.method == "POST":
 
            miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  profe = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
                  profe.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = ProfesorFormulario()  #mostramos un formulario vacio
 
      return render(request, "AppCoder/crear_profes.html", {"miFormulario": miFormulario})

#SEARCH - Busqueda individual de profesores
def buscar_profes(request):
    return render(request, "AppCoder/buscar_profes.html")

def resultado_profes(request):
    #mensaje = f"estoy buscando el profesor de apellido {request.GET['apellido']}"
    #return HttpResponse(f"estoy buscando el profesor de apellido {request.GET['apellido']}")
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        profesor_resultado = Profesor.objects.filter(apellido__iexact=apellido)
        
        return render(request, "AppCoder/resultado_profes.html", {"apellido": apellido, "res":profesor_resultado})
    
    else: 
        return HttpResponse("No Enviaste datos")
 
    return render(request, "AppCoder/resultado_profes.html")

def eliminar_profes(request, profesor_nombre):
    profesor_seleccionado = Profesor.objects.get(nombre = profesor_nombre)
    profesor_seleccionado.delete()
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/ver_profes.html",{"res":profesores})

def actualizar_profes(request, profesor_nombre):
    pass
  
############################################################################################################################################
#CRUD DE CURSOS  --- CLASICO
#READ ALL  -- Cargar todos los cursos en la pagina principal de CURSOS
def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/ver_cursos.html", {"res":cursos})

#CREATE -- Crear un nuevo Curso
def crear_cursos(request):
    if request.method == 'POST':
        curso =  Curso(nombre=request.POST['nombre'], comision=request.POST['comision'])
        curso.save()
        return render(request, "AppCoder/inicio.html")
 
    return render(request, "AppCoder/crear_cursos.html")