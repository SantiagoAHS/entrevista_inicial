# mi_aplicacion/models.py
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
