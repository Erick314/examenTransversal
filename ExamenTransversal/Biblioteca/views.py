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
