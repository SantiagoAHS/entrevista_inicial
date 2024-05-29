from django import forms
from .models import Estudiante

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=Estudiante.SEXO_CHOICES),
            'estado_civil': forms.Select(choices=Estudiante.ESTADO_CIVIL_CHOICES),
            'tipo_casa': forms.Select(choices=Estudiante.TIPO_CASA_CHOICES),
            'forma_trabajar': forms.Select(choices=Estudiante.FORMA_TRABAJAR_CHOICES),
            'tipo_computadora': forms.Select(choices=Estudiante.TIPO_COMPUTADORA_CHOICES),
            # Añadir más widgets personalizados si es necesario
        }
