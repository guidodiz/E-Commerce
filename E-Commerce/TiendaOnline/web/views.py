from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from .models import Productos

def index(request):
    time = now()
    productos = Productos.objects.filter(tiene_descuento=True)

    context = {
        'time': time,
        'productos': productos
    }

    return render(request, 'web/index.html', context)

def productos(request):
    time = now()
    productos = Productos.objects.all()

    context = {
        'time': time,
        'productos': productos
    }
    
    return render(request, 'web/productos.html', context)

def novedades(request):
    time = now()

    context = {
        'time': time,
    }

    return render(request, 'web/novedades.html', context)

def vista_producto(request, id):
    time = now()
    producto = Productos.objects.get(id=id)
    
    context = {
        'time': time,
        'producto': producto
    }

    return render(request, 'web/vista_producto.html', context)