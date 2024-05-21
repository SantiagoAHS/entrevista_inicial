# mi_aplicacion/forms.py
from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField()
