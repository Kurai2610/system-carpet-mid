from django.contrib import admin
from .models import Proveedor, MateriaPrima, MateriaPorProveedor, OrdenMaterial, DetalleOrden

admin.site.register(Proveedor)
admin.site.register(MateriaPrima)
admin.site.register(MateriaPorProveedor)
admin.site.register(OrdenMaterial)
admin.site.register(DetalleOrden)
