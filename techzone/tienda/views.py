from django.http import JsonResponse
from .models import Categoria


def lista_categorias(request):
    # 1. Recuperamos los datos que acabas de crear en el admin
    categorias = Categoria.objects.all()

    # 2. Elegimos qué campos queremos enviar (id, nombre y slug)
    data = list(categorias.values('id', 'nombre', 'slug'))

    # 3. Respondemos con JSON
    return JsonResponse(data, safe=False)