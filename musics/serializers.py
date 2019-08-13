# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/13 0013  下午 5:19 
# 文件名称   ：serializers.PY
# 开发工具   ：PyCharm
from rest_framework import serializers

from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')