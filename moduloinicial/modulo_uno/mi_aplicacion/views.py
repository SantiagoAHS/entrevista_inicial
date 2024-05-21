# mi_aplicacion/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# mi_aplicacion/views.py
from django.shortcuts import render
from .forms import PersonaForm

def formulario_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            # Aquí podrías guardar los datos en la base de datos
            # persona = form.save()
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            edad = form.cleaned_data['edad']
            # Mostrar los datos en la consola como un ejemplo de "guardar falsamente"
            print(f'Nombre: {nombre}, Email: {email}, Edad: {edad}')
            return render(request, 'formulario.html', {'form': form, 'enviado': True})
    else:
        form = PersonaForm()
    return render(request, 'formulario.html', {'form': form})

