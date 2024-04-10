from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import MarcaVehiculo, TipoVehiculo, ModeloVehiculo, CategoriaProducto, Producto


class MarcaVehiculoResource(resources.ModelResource):
    class Meta:
        model = MarcaVehiculo


class TipoVehiculoResource(resources.ModelResource):
    class Meta:
        model = TipoVehiculo


class ModeloVehiculoResource(resources.ModelResource):
    class Meta:
        model = ModeloVehiculo


class CategoriaProductoResource(resources.ModelResource):
    class Meta:
        model = CategoriaProducto


class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto


@admin.register(MarcaVehiculo)
class MarcaVehiculoAdmin(ImportExportModelAdmin):
    resource_class = MarcaVehiculoResource


@admin.register(TipoVehiculo)
class TipoVehiculoAdmin(ImportExportModelAdmin):
    resource_class = TipoVehiculoResource


@admin.register(ModeloVehiculo)
class ModeloVehiculoAdmin(ImportExportModelAdmin):
    resource_class = ModeloVehiculoResource


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(ImportExportModelAdmin):
    resource_class = CategoriaProductoResource


@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
