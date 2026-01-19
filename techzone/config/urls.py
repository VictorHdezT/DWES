from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tienda.views import lista_categorias, ProductoViewSet

# Configuración del Router
router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorias/', lista_categorias),

    # El router genera:
    # /api/productos/ (GET, POST)
    # /api/productos/ID/ (GET, PUT, DELETE)
    path('api/', include(router.urls)),
]