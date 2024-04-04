from django.shortcuts import render
from .models import Producto


def index(request):
    return render(request, 'index.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})
