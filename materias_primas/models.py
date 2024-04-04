from django.db import models
from common.models import Direccion, Articulo


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.OneToOneField(Direccion, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# materias primas tiene sus campos en el modelo articulo, ya que tiene datos redundantes


class MateriaPrima(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.PROTECT)

    def __str__(self):
        return self.articulo.nombre


class MateriaPorProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT)
    precio_unitario = models.PositiveIntegerField()


class OrdenMaterial(models.Model):
    precio_total = models.PositiveIntegerField()
    fecha = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Orden de material {self.id}'


class DetalleOrden(models.Model):
    orden = models.ForeignKey(OrdenMaterial, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(
        MateriaPorProveedor, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
