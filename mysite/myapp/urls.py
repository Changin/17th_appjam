from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:board_id>/', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    
    path('date/', views.date, name='date_picker'),
    path('clock/', views.clock, name='clock'),
    path('post/', views.post, name='post'),
    path('register/', views.register, name='register'),
    path('write/', views.write, name='write'),
]