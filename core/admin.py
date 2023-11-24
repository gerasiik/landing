from django.contrib import admin
from .models import Cursos
from .models import Estudiantes
from .models import Profesores
from .models import Entregable

# Register your models here.

admin.site.register(Cursos)
admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Entregable)
