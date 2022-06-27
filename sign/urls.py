from django.urls import path

from . import views

urlpatterns = [
    path('whiteList/', views.getCoupon, name='index'),
]