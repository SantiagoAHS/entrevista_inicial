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

# mi_aplicacion/forms.py

from django import forms
from .models import Profesor, Carrera, Grupo

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'carrera', 'grupo_tutor']
        widgets = {
            'carrera': forms.Select(attrs={'id': 'id_carrera'}),
            'grupo_tutor': forms.Select(attrs={'id': 'id_grupo_tutor'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['grupo_tutor'].queryset = Grupo.objects.none()

        if 'carrera' in self.data:
            try:
                carrera_id = int(self.data.get('carrera'))
                self.fields['grupo_tutor'].queryset = Grupo.objects.filter(carrera_id=carrera_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # carrera_id no es válido, no hacer nada
        elif self.instance.pk:
            self.fields['grupo_tutor'].queryset = self.instance.carrera.grupo_set.order_by('nombre')

from django import forms
from .models import Carrera, Grupo

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre']

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'carrera']





