from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('offers/', views.index, name='index'),
]
