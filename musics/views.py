from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from musics.models import Music
from musics.serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
