from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppTerceraEntrega.models import Alumno, Curso, Profesor
from AppTerceraEntrega.forms import AlumnoFormulario, ProfesorFormulario, CursoFormulario

# Create your views here.

def inicio(req):
    return render(req, 'appterceraentrega/padre.html')

def alumnos(req):
    alumno_buscado = ""
    if req.method == 'POST':
        formulaio = AlumnoFormulario(req.POST)

        if formulaio.is_valid():
            informacion = formulaio.cleaned_data
            alumno = Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            alumno.save()
            return redirect('alumnos')
    else:
        if req.GET.get("id"):
            id_alumno = req.GET["id"]
            alumno_buscado = Alumno.objects.filter(id=id_alumno).first()
            #Verifico que alumno_buscado sea de la clase Alumno
            if not isinstance(alumno_buscado, Alumno):
                alumno_buscado = ""

        formulaio = AlumnoFormulario()

    alumnos = Alumno.objects.all()
    return render(req, "appterceraentrega/alumnos.html",{"formulario": formulaio, "alumnos": alumnos, "alumno": alumno_buscado})


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
