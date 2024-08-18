from django.http import HttpResponse
from AppTerceraEntrega.models import Alumno, Curso, Profesor

def agregar_alumno(request, nom, ap, direccion_mail):
    alumno = Alumno(nombre = nom, apellido = ap, mail = direccion_mail)
    alumno.save()
    
    return HttpResponse("Alumno Agregado!!")

def agregar_curso(request, nom, cam):
    curso = Curso(nombre = nom, camada = cam)
    curso.save()
    
    return HttpResponse("Curso Agregado!!")

def agregar_profesor(request, nom, ap, prof):
    profesor = Profesor(nombre = nom, apellido = ap, profesion = prof)
    profesor.save()
    
    return HttpResponse("Profesor Agregado!!")