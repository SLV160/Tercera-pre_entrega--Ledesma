from django.shortcuts import render, redirect
from .models import Clase1, Clase2, Clase3
from .forms import Clase1Form, Clase2Form, Clase3Form
from django.shortcuts import render
from .models import Modelo

def crear_clase1(request):
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = Clase1Form()
    return render(request, 'crear_clase1.html', {'form': form})


def buscar(request):
    resultados = None

    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        query = request.POST.get('busqueda', None)

        if query:
            # Realiza la búsqueda en la base de datos
            resultados = Modelo.objects.filter(campo__icontains=query)

    return render(request, 'buscar.html', {'resultados': resultados})

def exito(request):
    return render(request, 'exito.html')