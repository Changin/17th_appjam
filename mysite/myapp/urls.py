from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:board_id>/', views.index, name='index'),
    path('login/', views.login_user, name='login'),
]