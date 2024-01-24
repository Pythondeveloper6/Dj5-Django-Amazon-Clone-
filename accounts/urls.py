from django.urls import path 
from .views import signup , user_activate



urlpatterns = [
    path('signup',signup) , 
    path('<str:username>/activate', user_activate),
]
