from django import forms

class AlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    mail= forms.CharField(max_length=50)