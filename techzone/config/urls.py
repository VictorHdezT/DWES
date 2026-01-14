from django.contrib import admin
from django.urls import path
from tienda.views import lista_categorias  # Importamos tu nueva vista

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta es la dirección web que escribiremos en el navegador
    path('api/categorias/', lista_categorias),
]

