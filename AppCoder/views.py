from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor
from AppCoder.models import Curso
from AppCoder.models import Estudiante
from AppCoder.forms import ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
@login_required
def inicio(request):
    nombre = 'fabian'
    return render(request, "AppCoder/inicio.html",{"name":nombre})

def ver_entregas(request):
    return render(request, "AppCoder/ver_entregas.html")

def ver_estudiantes(request):
    return render(request, "AppCoder/ver_estudiantes.html")

#############################################################################################################################
#lOGIN
def login_view(request):
    if request.method == "POST":
        form_inicio = AuthenticationForm(request, data = request.POST)
        
        if form_inicio.is_valid():
            info = form_inicio.cleaned_data
            usuario = info.get("username")
            contra = info.get("password")
            
            #aca hacemos la validacion
            user = authenticate(username=usuario, password=contra) #existe o no existe el usuario
            
            if user:
                login(request, user) #iniciar sesion si credenciales correctas.
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}","user":user})
            else:
                return render(request, "AppCoder/inicio.html",  {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form_inicio = AuthenticationForm()    
    return render(request, "AppCoder/login.html", {"res":form_inicio})

#REGISTER
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" , {"res":form})





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

def eliminar_profes(request, profesor_id):
    profesor_seleccionado = Profesor.objects.get(id = profesor_id)
    profesor_seleccionado.delete()
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/ver_profes.html",{"res":profesores})

def actualizar_profes(request, profesor_id):
    profesor_seleccionado = Profesor.objects.get(id=profesor_id)
    
    if request.method == "POST":  #hacemos click al boton actualizar
 
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            profesor_seleccionado.nombre = info["nombre"]
            profesor_seleccionado.apellido = info["apellido"]
            profesor_seleccionado.email = info["email"]
            profesor_seleccionado.profesion = info["profesion"]
            profesor_seleccionado.save()
                  
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario(initial={"nombre":profesor_seleccionado.nombre,
                                                    "apellido":profesor_seleccionado.apellido,
                                                    "email":profesor_seleccionado.email,
                                                    "profesion":profesor_seleccionado.profesion})  #mostramos el formulario con la informacion previa
 
    return render(request, "AppCoder/editar_profes.html", {"miFormulario": miFormulario})

    
    
  
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


###################################################################################################################################################
#CRUD
#Vista basada en clases

#Read
class EstudianteLista(LoginRequiredMixin, ListView): #estudiante_list.html
    model = Estudiante
    #template_name = "AppCoder/estudiante_form.html" #si no se quiere usar el nombre por defecto, se especifica asi.
    
#create
class EstudianteCrear(CreateView,LoginRequiredMixin):  #estudiante_form.html
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = "/AppCoder/estudiantes/lista/"

#update
class EstudianteActualizar(UpdateView):#estudiante_form.html
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = "/AppCoder/estudiantes/lista/"
    
class EstudianteBorrar(DeleteView):#estudiante_confirm_delete.html
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = "/AppCoder/estudiantes/lista/"

#detail
class EstudianteDetalle(DetailView):  #estudiante_detail.html
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = "/AppCoder/estudiantes/lista/"
