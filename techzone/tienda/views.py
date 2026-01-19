from django.http import JsonResponse
from .models import Categoria
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto


def lista_categorias(request):
    # 1. Recuperamos los datos que acabas de crear en el admin
    categorias = Categoria.objects.all()

    # 2. Elegimos qué campos queremos enviar (id, nombre y slug)
    data = list(categorias.values('id', 'nombre', 'slug'))

    # 3. Respondemos con JSON
    return JsonResponse(data, safe=False)


class ProductoListAPIView(APIView):
    def get(self, request):
        # 1. Buscar datos en la BD
        productos = Producto.objects.all()

        # 2. Convertir a lista de diccionarios
        data = []
        for p in productos:
            data.append({
                'id': p.id,
                'nombre': p.nombre,
                'precio': p.precio,
                'activo': p.activo
            })

        # 3. Responder con Response (DRF se encarga del JSON)
        return Response(data)