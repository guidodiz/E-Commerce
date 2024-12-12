from django.contrib import admin
from .models import Productos, Compras, Cliente

admin.site.register(Productos)
admin.site.register(Compras)
admin.site.register(Cliente)