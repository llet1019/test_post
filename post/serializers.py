from rest_framework import serializers
from .models import Post, Board


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'view_count',
            'created_at'
        )


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        field = (
            'id',
            'board_name'
        )
