from django.shortcuts import render
from rest_framework import generics

from .serializers import BoardSerializer, PostSerializer
from .models import Board, Post


class BoardList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
