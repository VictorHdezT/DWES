from django.http import JsonResponse
from .models import Categoria
from rest_framework import status # Para códigos HTTP (201, 400, etc)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer


def lista_categorias(request):
    # 1. Recuperamos los datos que acabas de crear en el admin
    categorias = Categoria.objects.all()

    # 2. Elegimos qué campos queremos enviar (id, nombre y slug)
    data = list(categorias.values('id', 'nombre', 'slug'))

    # 3. Respondemos con JSON
    return JsonResponse(data, safe=False)


class ProductoListAPIView(APIView):
    # GET: Listar
    def get(self, request):
        productos = Producto.objects.all()
        # many=True porque es una lista de productos
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    # POST: Crear
    def post(self, request):
        # Le pasamos los datos que envía el usuario (request.data)
        serializer = ProductoSerializer(data=request.data)

        # Validación automática
        if serializer.is_valid():
            serializer.save()  # Guarda en la BD
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # precio negativo o texto vacío
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)