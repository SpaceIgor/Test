from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
   path('user', views.userCreate, name='user'),
   path('user-list', views.userList, name='user-list'),
   path('user/<str:pk>', views.userDetail, name='user-detail'),

    ]


