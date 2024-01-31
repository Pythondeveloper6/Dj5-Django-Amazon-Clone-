from django.urls import path 
from .views import signup , user_activate , dashboard



urlpatterns = [
    path('signup',signup) , 
    path('dashboard',dashboard) , 
    path('<str:username>/activate', user_activate),
]
