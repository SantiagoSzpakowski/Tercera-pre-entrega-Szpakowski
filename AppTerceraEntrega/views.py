from django.shortcuts import render
from django.http import HttpResponse
from AppTerceraEntrega.models import Alumno, Curso, Profesor
from AppTerceraEntrega.forms import AlumnoFormulario

# Create your views here.

def inicio(req):
    return render(req, 'appterceraentrega/padre.html')

def profesores(req):    
    if req.method == 'POST':
        alumno = Profesor(nombre=req.POST['nombre'], apellido=req.POST['apellido'], profesion=req.POST['profesion'])
        alumno.save()
        return render(req,"appterceraentrega/padre.html")

    return render(req,"appterceraentrega/profesores.html")

def cursos(req):
    if req.method == 'POST':
        curso = Curso(nombre=req.POST['nombre'], camada=req.POST['camada'])
        curso.save()
        return render(req,"appterceraentrega/padre.html")

    return render(req,"appterceraentrega/cursos.html")

def alumnos(req):
    if req.method == 'POST':
        formulaio = AlumnoFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            alumno = Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            alumno.save()
            return render(req,"appterceraentrega/padre.html")
    else:
        formulaio = AlumnoFormulario()

    return render(req, "appterceraentrega/alumnos.html",{"formulario": formulaio})