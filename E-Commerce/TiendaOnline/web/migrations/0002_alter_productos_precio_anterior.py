# Generated by Django 5.1.3 on 2024-12-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio_anterior',
            field=models.CharField(blank=True, max_length=11, verbose_name='Precio anterior'),
        ),
    ]
