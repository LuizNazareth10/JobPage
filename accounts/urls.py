from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
