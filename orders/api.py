from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import CartDetailSerializer,CartSerializer,OrderDetailSerializer,OrderSerializer
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
from products.models import Product
from settings.models import DeliveryFee


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    
    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()
        user = User.objects.get(username=self.kwargs['username'])
        queryset = queryset.filter(user=user)
        return queryset
    
    
    # def list(self,request,*args, **kwargs):
    #     queryset = super(OrderListAPI, self).get_queryset()
    #     user = User.objects.get(username=self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     data = OrderSerializer(queryset,many=True).data
    #     return Response({'orders':data})
    
    
    
class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()