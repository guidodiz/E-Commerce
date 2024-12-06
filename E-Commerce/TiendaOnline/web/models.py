from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio anterior')
    precio_nuevo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio nuevo')