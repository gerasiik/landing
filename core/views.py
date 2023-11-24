from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def inicio(request):
    return render(request, "core/inicio.html")


def cursos(request):
    return render(request, "core/cursos.html")


def estudiantes(request):
    return render(request, "core/estudiantes.html")


def entregables(request):
    return render(request, "core/entregables.html")
