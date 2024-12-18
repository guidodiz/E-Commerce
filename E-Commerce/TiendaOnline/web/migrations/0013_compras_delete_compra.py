# Generated by Django 5.1.3 on 2024-12-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_compra_medio_de_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=255, verbose_name='Producto')),
                ('talle', models.CharField(max_length=50, verbose_name='Talle')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.CharField(max_length=15, verbose_name='Precio')),
                ('medio_de_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('MP', 'Mercado Pago'), ('Transferencia', 'Transferencia Bancaria')], max_length=25)),
                ('envio', models.CharField(blank=True, choices=[('Envío', 'Envío'), ('Retiro', 'Retiro')], max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
    ]
