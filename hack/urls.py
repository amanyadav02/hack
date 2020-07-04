from django.contrib import admin
from django.urls import path,include
from hack import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.logindevta,name='login'),
    path('register/',views.register,name='register'),
]
