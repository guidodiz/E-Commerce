from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio_anterior = models.CharField(max_length=11, verbose_name='Precio anterior')
    precio_nuevo = models.CharField(max_length=11, verbose_name='Precio nuevo')
    imagen = models.ImageField(upload_to='productos/', verbose_name='Imagen')

    def __str__(self):
        return f'{self.nombre}'