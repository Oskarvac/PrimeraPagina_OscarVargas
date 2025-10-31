from django import forms
from .models import Producto, Categoria, Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class BusquedaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
