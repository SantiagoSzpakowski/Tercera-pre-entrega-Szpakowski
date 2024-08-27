from django.http import HttpResponse
from django.shortcuts import redirect


def redirigir_AppTerceraEntrega_Inicio(req):
    return redirect('inicio')