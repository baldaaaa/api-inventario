from django import forms
from .models import Carpeta, Item

class CarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = ('nombre',)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'nombre',
            'cantidad',
        )