from .models import Compra
from django import forms


class CompraModelForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['producto', 'talle', 'cantidad', 'precio', 'medio_de_pago']