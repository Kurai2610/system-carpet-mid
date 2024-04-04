from django.contrib import admin
from .models import MarcaVehiculo, TipoVehiculo, ModeloVehiculo, CategoriaProducto, Producto

admin.site.register(MarcaVehiculo)
admin.site.register(TipoVehiculo)
admin.site.register(ModeloVehiculo)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
