# Generated by Django 5.1.3 on 2024-12-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_remove_compra_fecha_compra_medio_de_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='medio_de_pago',
            field=models.CharField(max_length=25, verbose_name='Medio de pago'),
        ),
    ]
