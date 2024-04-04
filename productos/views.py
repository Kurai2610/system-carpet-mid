from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def productos(request):
    return render(request, 'productos.html')


def detalle_producto(request, producto_id):
    return render(request, 'detalle_producto.html', {'producto_id': producto_id})
