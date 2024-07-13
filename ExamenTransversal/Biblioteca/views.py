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
    context = {}
    return render(request, 'Biblioteca/libros.html', context)

def buscar_libros(request):
    query = request.GET.get('query', '')
    libros = Libro.objects.filter(
        models.Q(tituloicontains=query) |
        models.Q(anioPublicacionicontains=query) |
        models.Q(descripcion__icontains=query)
    )
    results = [
        {
            'idLibro': libro.idLibro,
            'titulo': libro.titulo,
            'anioPublicacion': libro.anioPublicacion,
            'descripcion': libro.descripcion
        }
        for libro in libros
    ]
    return JsonResponse(results, safe=False)
