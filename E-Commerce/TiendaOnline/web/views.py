from django.shortcuts import render
from django.http import HttpResponse
from .models import Productos

def index(request):
    productos = Productos.objects.filter(tiene_descuento=True)

    context = {
        'productos': productos
    }

    return render(request, 'web/index.html', context)

def productos(request):
    productos = Productos.objects.all()

    context = {
        'productos': productos
    }
    
    return render(request, 'web/productos.html', context)

def novedades(request):
    return render(request, 'web/novedades.html')