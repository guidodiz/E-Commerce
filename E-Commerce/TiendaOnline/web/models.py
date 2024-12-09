from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio_original = models.CharField(max_length=15, verbose_name='Precio original', blank=True)
    precio_anterior = models.CharField(max_length=15, verbose_name='Precio anterior', blank=True)
    precio_nuevo = models.CharField(max_length=15, verbose_name='Precio nuevo', blank=True)
    tiene_descuento = models.BooleanField(default=False, verbose_name='Tiene descuento?')
    imagen = models.ImageField(upload_to='productos/', verbose_name='Imagen')

    def __str__(self):
        return f'{self.nombre}'