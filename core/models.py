from django.db import models

# Create your models here.


class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emails = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
