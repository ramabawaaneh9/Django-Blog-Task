from rest_framework import serializers
from ..models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')