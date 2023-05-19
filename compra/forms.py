from django import forms
from .models import Proveedor, Producto


class ProveedorForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    dni = forms.IntegerField(label='DNI')

class ProductoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    precio = forms.IntegerField(label='Precio')    
    stock_actual = forms.IntegerField(label='Stock_actual') 
    proveedor = forms.IntegerField(label='proveedor')