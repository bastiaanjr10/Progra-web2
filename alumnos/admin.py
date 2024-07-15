from django.contrib import admin
from .models import tipoUsuario, Usuario, tipoProducto, Producto
# Register your models here.

admin.site.register(tipoUsuario)
admin.site.register(Usuario)
admin.site.register(tipoProducto)
admin.site.register(Producto)
