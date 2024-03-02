from django.contrib import admin
from .models import Producto, Proveedor, Compra, Categoria, Marca, CompraProducto, Post

# Register your models here.
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(CompraProducto)
admin.site.register(Post)