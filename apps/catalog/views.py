from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemCreateSerializer

class ItemCreateAPIView(APIView):
    """
    Endpoint для добавления нового предмета.
    Проверяет уникальность комбинации: tenant_id + category_id + inventory_number.
    """

    def post(self, request):
        print('-----')
        print('---')
        print(request.data)
        # Получаем ключевые поля из входящих данных
        tenant_id = request.data.get('tenant_id')
        category_id = request.data.get('category_id')
        inventory_number = request.data.get('inventory_number')

        # Проверяем, все ли поля переданы
        if not tenant_id or not category_id or not inventory_number:
            return Response(
                {
                    'error': 'Обязательны поля: tenant_id, category_id, inventory_number.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Проверяем, существует ли уже запись с такой тройкой значений
        if Item.objects.filter(
                tenant_id=tenant_id,
                category_id=category_id,
                inventory_number=inventory_number
        ).exists():
            return Response(
                {
                    'error': (
                        f'У вашей организации в категории {category_id} '
                        f'инвентарный номер {inventory_number} уже существует.'
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

            # Если проверки прошли — продолжаем стандартную обработку
        serializer = ItemCreateSerializer(data=request.data)
        print('====')
        print(serializer)
        if serializer.is_valid():
            item = serializer.save()
            return Response(
                ItemCreateSerializer(item).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import Item


class ItemListAPIView(APIView):
    """
    GET /api/items/list/
    Возвращает список всех предметов клиента (tenant_id)
    """

    def get(self, request):
        # Для MVP tenant_id передаем через query params
        tenant_id = request.query_params.get('tenant_id')
        if not tenant_id:
            return Response({"detail": "tenant_id is required"}, status=400)

        items = Item.objects.filter(tenant_id=tenant_id)
        serializer = ItemCreateSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetailAPIView(APIView):
    """
    GET / PATCH / DELETE /api/items/{id}/
    """

    def get_object(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return None

    def get(self, request, item_id):
        item = self.get_object(item_id)
        if not item:
            return Response({"detail": "Item not found"}, status=404)
        serializer = ItemCreateSerializer(item)
        return Response(serializer.data)

    def patch(self, request, item_id):
        item = self.get_object(item_id)
        if not item:
            return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        # Получаем новые значения из request.data (если они переданы)
        new_tenant_id = request.data.get('tenant_id', item.tenant_id)
        new_category_id = request.data.get('category_id', item.category_id)
        new_inventory_number = request.data.get('inventory_number', item.inventory_number)

        # Проверяем, не совпадает ли новая комбинация с существующей записью (кроме текущей)
        if Item.objects.filter(
            tenant_id=new_tenant_id,
            category_id=new_category_id,
            inventory_number=new_inventory_number
        ).exclude(id=item.id).exists():
            return Response(
                {
                    'error': (
                        'Запись с такими inventory_number уже существует.'
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Если проверка пройдена — продолжаем обновление
        serializer = ItemCreateSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        item = self.get_object(item_id)
        if not item:
            return Response({"detail": "Item not found"}, status=404)

        item.delete()
        return Response(status=204)
