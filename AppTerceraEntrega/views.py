from django.shortcuts import render, redirect
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
            return redirect('alumnos')
    else:
        formulaio = AlumnoFormulario()

    alumnos = Alumno.objects.all()
    return render(req, "appterceraentrega/alumnos.html",{"formulario": formulaio, "alumnos": alumnos})


def profesores(req):    
    if req.method == 'POST':
        formulaio = ProfesorFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], profesion=informacion['profesion'])
            profesor.save()
            return redirect('profesores')
    else:
        formulaio = ProfesorFormulario()

    profesores = Profesor.objects.all()
    return render(req, "appterceraentrega/profesores.html",{"formulario": formulaio, "profesores": profesores})

def cursos(req):
    if req.method == 'POST':
        formulaio = CursoFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return redirect('cursos')
    else:
        formulaio = CursoFormulario()

    cursos = Curso.objects.all()
    return render(req, "appterceraentrega/cursos.html",{"formulario": formulaio, "cursos": cursos})
