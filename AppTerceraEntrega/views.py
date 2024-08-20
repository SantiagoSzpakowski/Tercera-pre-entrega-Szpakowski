from django.shortcuts import render
from django.http import HttpResponse
from AppTerceraEntrega.models import Alumno, Curso, Profesor
from AppTerceraEntrega.forms import AlumnoFormulario, ProfesorFormulario, CursoFormulario

# Create your views here.

def inicio(req):
    return render(req, 'appterceraentrega/padre.html')

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

def profesores(req):    
    if req.method == 'POST':
        formulaio = ProfesorFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], profesion=informacion['profesion'])
            profesor.save()
            return render(req,"appterceraentrega/padre.html")
    else:
        formulaio = ProfesorFormulario()

    return render(req, "appterceraentrega/profesores.html",{"formulario": formulaio})

def cursos(req):
    if req.method == 'POST':
        formulaio = CursoFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(req,"appterceraentrega/padre.html")
    else:
        formulaio = CursoFormulario()

    return render(req, "appterceraentrega/cursos.html",{"formulario": formulaio})
