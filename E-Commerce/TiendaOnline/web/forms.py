from .models import Compras
from django import forms


class CompraModelForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['producto', 'talle', 'cantidad', 'precio', 'medio_de_pago', 'envio', 'cliente']