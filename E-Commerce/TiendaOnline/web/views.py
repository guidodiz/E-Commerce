from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'web/index.html')

def productos(request):
    return render(request, 'web/productos.html')

def contacto(request):
    return render(request, 'web/contacto.html')