from rest_framework import serializers
from .models import Item

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'tenant_id',
            'category_id',
            'title',
            'comment',
            'inventory_number',
            'attributes',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
