from django.shortcuts import render , redirect
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
from products.models import Product 
from settings.models import DeliveryFee

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request,'orders/order_list.html',{'orders':data})
    


def checkout(request):
    cart = Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    
    sub_total = cart.cart_total
    discount = 0
    total = sub_total + delivery_fee
    
    
    return render(request,'orders/checkout.html',{
        'cart_detail' : cart_detail , 
        'delivery_fee': delivery_fee , 
        'sub_total': sub_total , 
        'discount': discount , 
        'total': total
    })




def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail , created = CartDetail.objects.get_or_create(cart=cart,product=product)
    
    # if not created:
    #     cart_detail.quantity = cart_detail.quantity + quantity
    
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity,2)
    cart_detail.save()
    
    return redirect(f'/products/{product.slug}')
    