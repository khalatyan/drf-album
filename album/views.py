from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from album.models import Executor, Album, AlbumSong, Song
from album.serializers import ExecutorSerializer, SongSerializer, AlbumSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


