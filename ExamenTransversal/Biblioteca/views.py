from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request, 'Biblioteca/index.html', context)

def autores(request):
    q = request.GET.get('q', '')  
    if q:
        autores = Autor.objects.filter(nombre__icontains=q)  
    else:
        autores = Autor.objects.all()  
    
    context = {
        'autores': autores
    }
    return render(request, 'Biblioteca/autores.html', context)

def categorias(request):
    query = request.GET.get('q', '')
    if query:
        categorias = Categoria.objects.filter(nombre__icontains=query)
    else:
        categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'Biblioteca/categorias.html', context)

def libros(request):
    query = request.GET.get('q')  
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) 
    else:
        libros = Libro.objects.all() 
    
    context = {
        'libros': libros
    }
    return render(request, 'Biblioteca/libros.html', context)