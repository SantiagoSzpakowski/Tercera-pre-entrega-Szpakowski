from AppTerceraEntrega import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos')
]