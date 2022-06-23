from django.urls import path

from . import views

urlpatterns = [
    path('totalSupply/', views.querytotalSupply, name='index'),
]