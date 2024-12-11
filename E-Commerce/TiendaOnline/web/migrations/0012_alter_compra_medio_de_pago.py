# Generated by Django 5.1.3 on 2024-12-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_compra_medio_de_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='medio_de_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('MP', 'Mercado Pago'), ('Transferencia', 'Transferencia Bancaria')], max_length=25),
        ),
    ]
