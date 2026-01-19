from django.http import JsonResponse
from .models import Categoria
from rest_framework import status # Para códigos HTTP (201, 400, etc)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Producto
from .serializers import ProductoSerializer


def lista_categorias(request):
    # 1. Recuperamos los datos que acabas de crear en el admin
    categorias = Categoria.objects.all()

    # 2. Elegimos qué campos queremos enviar (id, nombre y slug)
    data = list(categorias.values('id', 'nombre', 'slug'))

    # 3. Respondemos con JSON
    return JsonResponse(data, safe=False)


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer