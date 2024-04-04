from django.contrib import admin
from .models import Localidad, Barrio, Direccion, TipoArticulo, Articulo

admin.site.register(Localidad)
admin.site.register(Barrio)
admin.site.register(Direccion)
admin.site.register(TipoArticulo)
admin.site.register(Articulo)
