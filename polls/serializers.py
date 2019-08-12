# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/12 0012  下午 4:19 
# 文件名称   ：serializers.PY
# 开发工具   ：PyCharm


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')