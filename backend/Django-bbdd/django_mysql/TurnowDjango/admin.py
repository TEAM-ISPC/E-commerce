from django.contrib import admin
from .models import Usuario
from .models import Emprendedor
from .models import Cliente
from .models import Categoria
from .models import Producto

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display =("id_Usuario","apellidoUsuario","nombreUsuario","emailUsuario","rolUsuario")

class EmprendedorAdmin(admin.ModelAdmin):
    list_display =("nombreEmprendimiento","usuario_id")

class ClienteAdmin(admin.ModelAdmin):
    list_display =("id_Cliente","usuario_id")

class ProductoAdmin(admin.ModelAdmin):
    list_display =("nombreProducto","descripcionProducto","precioUnitario","cantidadProducto","codigodeBarras","imagenProducto","emprendedor_id","id_Categoria")

class CategoriaAdmin(admin.ModelAdmin):
    list_display =("nombreCategoria", "descripcionCategoria")

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Emprendedor,EmprendedorAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)