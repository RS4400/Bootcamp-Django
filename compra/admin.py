from django.contrib import admin
from .models import Proveedor
from .models import Producto

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido']
    list_filter = ['nombre','apellido']
    search_fields = ['nombre','apellido']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio', 'stock_actual']
    list_filter = ['nombre','precio', 'stock_actual']
    search_fields = ['nombre','precio', 'stock_actual']

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Proveedor, ProveedorAdmin)