from django.shortcuts import render

from django.views.generic import ListView , DetailView

from .models import Product , Brand , Review




# queryset : [products] : filter
# context : user

class ProductList(ListView):
    model = Product
    
    
    
# context{} , queryset : Product.objects.all() : 1 : option   2 : method : overide
# querset : main query : detail product       
# context : extra data  : reviews , images
    
class ProductDetail(DetailView):    
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # dict : object product
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
        