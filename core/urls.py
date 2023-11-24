from django.urls import path
from core import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("entregables/", views.entregables, name="entregables"),
]
