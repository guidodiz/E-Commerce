from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=110, verbose_name='Descripción', blank=True)
    talle1 = models.CharField(max_length=15, verbose_name='Talle 1', blank=True)
    talle2 = models.CharField(max_length=15, verbose_name='Talle 2', blank=True)
    talle3 = models.CharField(max_length=15, verbose_name='Talle 3', blank=True)
    talle4 = models.CharField(max_length=15, verbose_name='Talle 4', blank=True)
    talle5 = models.CharField(max_length=15, verbose_name='Talle 5', blank=True)
    precio_original = models.CharField(max_length=15, verbose_name='Precio original', blank=True)
    precio_anterior = models.CharField(max_length=15, verbose_name='Precio anterior', blank=True)
    precio_nuevo = models.CharField(max_length=15, verbose_name='Precio nuevo', blank=True)
    tiene_descuento = models.BooleanField(default=False, verbose_name='Tiene descuento?')
    imagen = models.ImageField(upload_to='productos/', verbose_name='Imagen')
    imagen2 = models.ImageField(upload_to='productos/', verbose_name='Imagen 2', blank=True)
    imagen3 = models.ImageField(upload_to='productos/', verbose_name='Imagen 3', blank=True)
    imagen4 = models.ImageField(upload_to='productos/', verbose_name='Imagen 4', blank=True)

    def __str__(self):
        return f'{self.nombre}'

class Compra(models.Model):
    producto = models.CharField(max_length=255, verbose_name='Producto')
    talle = models.CharField(max_length=50, verbose_name='Talle')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.CharField(max_length=15, verbose_name='Precio')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de compra')

    def __str__(self):
        return f'{self.producto} | talle: {self.talle} | cantidad: {self.cantidad}'