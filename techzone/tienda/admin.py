from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

# Registramos los modelos simples
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)

# Configuración especial para ver los detalles dentro del pedido
class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]
    list_display = ('id', 'cliente', 'fecha', 'estado')