from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField(max_length=50)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=50)