from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={
        'nombre': 'Guido'
    }
    return render(request, 'web/index.html', context)