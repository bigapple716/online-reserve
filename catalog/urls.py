from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve/', views.reserve, name='reserve'),    # reserve
    path('inquiry/', views.inquiry, name='inquiry'),    # inquiry
    path('reserve-success/', views.reserve_success, name='reserve-success'),
    path('inquiry-success/', views.inquiry_success, name='inquiry-success'),
]