# -*- coding: utf-8 -*-

from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),  # 主页
    path('reserve/', views.reserve, name='reserve'),    # 预约界面
    path('inquiry/', views.inquiry, name='inquiry'),    # 查询界面
    path('reserve-success/', views.reserve_success, name='reserve-success'),  # 预约成功界面
    path('inquiry-success/', views.inquiry_success, name='inquiry-success'),  # 查询成功界面
]