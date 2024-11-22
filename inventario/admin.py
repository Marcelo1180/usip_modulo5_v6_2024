from django.contrib import admin
from .models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'disponible')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('disponible','categoria',)

admin.site.register(Producto, ProductoAdmin)