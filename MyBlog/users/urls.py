# -*- coding = utf-8 -*-
# @Time : 2022/8/25 15:14
# @Author : 栀夏
# @File : urls.py
# @Software PyCharm
from django.urls import path
from users.views import RigisterView
# 进行users子应用的视图路由

urlpatterns = [
    path('register/',RigisterView.as_view(),name='register'),
]
