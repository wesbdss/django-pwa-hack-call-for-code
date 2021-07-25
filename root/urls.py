from django.contrib import admin
from django.urls import path,include
from . import views

app_name='root'
urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('myoffline/', views.offline,name='myoffline'),
]
