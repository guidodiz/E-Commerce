# Generated by Django 5.1.3 on 2024-12-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_productos_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='talle1',
            field=models.CharField(blank=True, max_length=15, verbose_name='Talle 1'),
        ),
        migrations.AddField(
            model_name='productos',
            name='talle2',
            field=models.CharField(blank=True, max_length=15, verbose_name='Talle 2'),
        ),
        migrations.AddField(
            model_name='productos',
            name='talle3',
            field=models.CharField(blank=True, max_length=15, verbose_name='Talle 3'),
        ),
        migrations.AddField(
            model_name='productos',
            name='talle4',
            field=models.CharField(blank=True, max_length=15, verbose_name='Talle 4'),
        ),
        migrations.AddField(
            model_name='productos',
            name='talle5',
            field=models.CharField(blank=True, max_length=15, verbose_name='Talle 5'),
        ),
    ]
