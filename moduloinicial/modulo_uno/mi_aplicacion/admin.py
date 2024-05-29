from django.contrib import admin

from .models import Carrera, Grupo, Profesor, Estudiante

admin.site.register(Carrera)
admin.site.register(Grupo)
admin.site.register(Profesor)
admin.site.register(Estudiante)

