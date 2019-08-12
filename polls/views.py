from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mysite.polls.serializers import UserSerializer, GroupSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
