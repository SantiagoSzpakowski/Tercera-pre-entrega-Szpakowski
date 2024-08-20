from django.shortcuts import render
from django.http import HttpResponse
from AppTerceraEntrega.models import Alumno, Curso, Profesor

# Create your views here.

def inicio(req):
    return render(req, 'appterceraentrega/padre.html')

def alumnos(req):
    
    if req.method == 'POST':
        print(req.POST)
        alumno = Alumno(nombre=req.POST['nombre'], apellido=req.POST['apellido'], mail=req.POST['mail'])
        
        alumno.save()
        return render(req,"appterceraentrega/padre.html")

    return render(req,"appterceraentrega/alumnos.html")
