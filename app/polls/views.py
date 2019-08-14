# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView

from app.polls import UserSerializer, GroupSerializer
from app.polls.models import Article


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

class login(APIView):
    def get(self,request,format=None):
        name=Article.objects.get(id=1)
        article_id=Article.article_id
        title=Article.title
        brief_content=Article.brief_content
        content=Article.content
        publish_date=Article.publish_date
        resp={
            'article_id':article_id,
            'title':title,
            'brief_content':brief_content,
            'content':content,
            'publish_date':publish_date,
        }





