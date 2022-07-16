from django.contrib import admin
from django.urls import path, include
from app import views 
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.registerPage,name='register'),
    path('',views.loginPage,name='login'),
    path('reset/',views.resetPage,name='reset'),
    path('home/',views.homePage,name='home')

   


   
]
