from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

# Create your views here.

def list_proveedores(request):

    try:

        proveedores = Proveedor.objects.all()

        context = {
            'proveedores': proveedores
        }

        return render(request, 'list_proveedores.html', context)

    except Exception:

        return render(request, 'errors_proveedor.html')
    
def create_proveedor(request):

    # Instancia de ProveedorForm
    form = ProveedorForm()

    if request.method == "POST":

        form = ProveedorForm(request.POST)

        if form.is_valid():

            proveedor = Proveedor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                dni=form.cleaned_data['dni'],

            )
            proveedor.save()

            return redirect('/list_proveedores/')

        else:
            return redirect('/list_proveedores/')

    context = {'form': form}
    
    return render(request, 'create_proveedor.html', context)

def list_productos(request):

    try:

        productos = Producto.objects.all()

        context = {
            'productos': productos
        }

        return render(request, 'list_productos.html', context)

    except Exception:

        return render(request, 'errors_producto.html')
    
def create_producto(request):

    # Instancia de ProveedorForm
    form = ProductoForm()

    if request.method == "POST":

        form = ProductoForm(request.POST)

        if form.is_valid():

            producto = Producto(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                stock_actual=form.cleaned_data['stock_actual'],
                proveedor=form.cleaned_data['proveedor']

            )
            producto.save()

            return redirect('/list_productos/')

        else:
            return redirect('/list_productos/')

    context = {'form': form}
    
    return render(request, 'create_producto.html', context)