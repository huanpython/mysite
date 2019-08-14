# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.musics.models import Music
from app.musics.serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
