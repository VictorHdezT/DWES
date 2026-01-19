from django.contrib import admin
from django.urls import path
from tienda.views import lista_categorias, ProductoListAPIView # Importamos la clase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorias/', lista_categorias),
    # Nueva URL para la clase
    path('api/productos/', ProductoListAPIView.as_view()),
]
