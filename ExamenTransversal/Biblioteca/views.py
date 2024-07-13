from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request, 'Biblioteca/index.html', context)

def autores(request):
    context = {}
    return render(request, 'Biblioteca/autores.html', context)

def categorias(request):
    context = {}
    return render(request, 'Biblioteca/categorias.html', context)

def libros(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda de la solicitud GET
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)  # Filtra los libros que contienen el término en el título
    else:
        libros = Libro.objects.all()  # Muestra todos los libros si no hay término de búsqueda
    
    context = {
        'libros': libros  # Pasa los libros filtrados o todos los libros a la plantilla
    }
    return render(request, 'Biblioteca/libros.html', context)