from django.shortcuts import render, redirect
from .models import Clase1, Clase2, Clase3
from .forms import Clase1Form, Clase2Form, Clase3Form

def crear_clase1(request):
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = Clase1Form()
    return render(request, 'crear_clase1.html', {'form': form})

# Repite este patrón para las otras clases y formularios

def buscar(request):
    if request.method == 'POST':
        # Implementa la lógica de búsqueda en la base de datos aquí
        # resultados = ...
    else:
        resultados = None
    return render(request, 'buscar.html', {'resultados': resultados})

def exito(request):
    return render(request, 'exito.html')
