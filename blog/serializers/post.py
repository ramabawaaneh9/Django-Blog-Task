from rest_framework import serializers

from ..models.post import Post
from ..models.category import Category


class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author',
            'category',
            'categories',
        )

        read_only_fields = (
            'id',
            'categories',
        )

    def create(self, validated_data):
        category = validated_data.pop('category')

        post = Post.objects.create(**validated_data)

        post.categories.add(category)

        return post