from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemCreateSerializer

class ItemCreateAPIView(APIView):
    """
    Endpoint для добавления нового предмета.
    """

    def post(self, request):
        serializer = ItemCreateSerializer(data=request.data)
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

class ItemDeleteAPIView(APIView):
    """
    DELETE /api/items/{id}/
    Удаляет предмет по id
    """

    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"detail": "Item not found"}, status=404)

        item.delete()
        # return Response({"detail": "Item deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Item deleted"}, status=status.HTTP_200_OK ) # 200 OK
