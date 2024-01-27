from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from utils.generate_code import generate_code
from products.models import Product
from accounts.models import Address

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
)

class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_owner',on_delete=models.SET_NULL , null=True,blank=True)
    status = models.CharField(choices=ORDER_STATUS , max_length=12)
    code = models.CharField(default=generate_code,max_length=20)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_address = models.ForeignKey(Address , related_name='delivery_address',on_delete=models.SET_NULL , null=True,blank=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total = models.FloatField()
    total_with_coupon = models.FloatField(null=True,blank=True)
    


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='orderdetail_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField(null=True,blank=True)



CART_STATUS = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_owner',on_delete=models.SET_NULL , null=True,blank=True)
    status = models.CharField(choices=CART_STATUS , max_length=12)
    coupon = models.ForeignKey('Coupon',related_name='cart_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)
    
    @property
    def cart_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.total
        return round(total,2)
    


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='cartdetail_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)





class Coupon(models.Model):
    code = models.CharField(max_length=20)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True,blank=True)
    quantity = models.IntegerField()
    discount = models.FloatField()
    
    def save(self, *args, **kwargs):
        if not self.end_date:
            week = datetime.timedelta(days=7) 
            self.end_date = self.start_date + week
        super(Coupon, self).save(*args, **kwargs) 