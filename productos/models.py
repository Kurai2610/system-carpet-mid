from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from common.models import Articulo

# Create your models here.


class MarcaVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas de Vehículos"


class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Vehículos"


class ModeloVehiculo(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField(validators=[MinValueValidator(
        1900), MaxValueValidator(datetime.date.today().year)])
    marca = models.ForeignKey(MarcaVehiculo, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.marca.nombre} - {self.año}"

    class Meta:
        verbose_name_plural = "Modelos de Vehículos"


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descuento = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías de Productos"


# el modelo articulo tiene datos comunes a todos los productos


class Producto(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloVehiculo, on_delete=models.PROTECT)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    link_imagen = models.URLField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.articulo.nombre} - {self.modelo.nombre} - {self.categoria.nombre}"

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
