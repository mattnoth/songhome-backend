from django.shortcuts import render
import datetime
from rest_framework import viewsets, filters
from .models import Song, Comment, Writer, Tag
from .serializers import SongSerializer, CommentSerializer, WriterSerializer, TagSerializer

# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'tags__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class TagViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
