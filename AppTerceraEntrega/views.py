from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(req):
    return render(req, 'appterceraentrega/padre.html')

def alumnos(req):
    return render(req, 'appterceraentrega/alumnos.html')