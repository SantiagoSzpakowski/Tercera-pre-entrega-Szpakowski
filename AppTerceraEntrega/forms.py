from django import forms

class AlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    mail= forms.EmailField(max_length=50)

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    profesion= forms.CharField(max_length=50)

class CursoFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    camada= forms.IntegerField()
