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
