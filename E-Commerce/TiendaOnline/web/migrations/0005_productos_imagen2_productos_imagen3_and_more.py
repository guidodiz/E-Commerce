# Generated by Django 5.1.3 on 2024-12-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_productos_tiene_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen2',
            field=models.ImageField(blank=True, upload_to='productos/', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen3',
            field=models.ImageField(blank=True, upload_to='productos/', verbose_name='Imagen 3'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen4',
            field=models.ImageField(blank=True, upload_to='productos/', verbose_name='Imagen 4'),
        ),
    ]
