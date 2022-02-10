from django.shortcuts import render
from rest_framework import generics

from .serializers import BoardSerializer, PostSerializer, PostDetailSerializer
from .models import Board, Post


class BoardList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'board_id'

    def get_queryset(self):
        board_id = self.kwargs.get(self.lookup_url_kwarg)
        return Post.objects.filter(board__id=board_id).order_by('-created_at')


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        return Post.objects.filter(id=post_id)
