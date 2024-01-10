from django.urls import path 
from .views import order_list , checkout , add_to_cart



urlpatterns = [
    path('' , order_list),
    path('checkout/' , checkout),
    path('add-to-cart',add_to_cart),
    
]
