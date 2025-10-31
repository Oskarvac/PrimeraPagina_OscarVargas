from django.shortcuts import render
from .forms import ProductoForm, CategoriaForm, MarcaForm, BusquedaForm
from .models import Producto

def home(request):
    return render(request, 'blog/home.html')

def agregar_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Producto'})

def agregar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Categoría'})

def agregar_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Marca'})

def buscar_producto(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Producto.objects.filter(nombre__icontains=nombre)
    else:
        form = BusquedaForm()
    return render(request, 'blog/busqueda.html', {'form': form, 'resultados': resultados})
