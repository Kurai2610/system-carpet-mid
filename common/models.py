from django.db import models


class Localidad(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'


class Barrio(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'


class Direccion(models.Model):
    detalles = models.CharField(max_length=100, null=True, blank=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.PROTECT)

    def __str__(self):
        return self.detalles

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'


class TipoArticulo(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    stock_minimo = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Articulo'
        verbose_name_plural = 'Tipos de Articulos'


class Articulo(models.Model):
    STOCK_CHOICES = (
        ('Agotado', 'Agotado'),
        ('Insuficiente', 'Insuficiente'),
        ('Disponible', 'Disponible'),
    )
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    cantidad = models.PositiveIntegerField(null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(TipoArticulo, on_delete=models.PROTECT)
    estado = models.CharField(
        max_length=12, choices=STOCK_CHOICES, default='Disponible')

    def save(self, *args, **kwargs):
        if self.cantidad <= self.tipo.stock_minimo:
            self.estado = 'Agotado'
        elif self.cantidad < self.tipo.stock_minimo * 2:
            self.estado = 'Insuficiente'
        else:
            self.estado = 'Disponible'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
