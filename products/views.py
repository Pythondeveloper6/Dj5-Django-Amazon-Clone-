from django.shortcuts import render , redirect

from django.views.generic import ListView , DetailView

from .models import Product , Brand , Review , ProductImages
from django.db.models import Q , F , Value
from django.db.models.aggregates import Count,Sum,Avg,Max,Min
from django.views.decorators.cache import cache_page

@cache_page(60 * 1)
def mydebug(request):
    # data = Product.objects.all()
    
    # column number  -------------
    # data = Product.objects.filter(price = 20)
    # data = Product.objects.filter(price__gt= 98)
    # data = Product.objects.filter(price__gte= 98)
    # data = Product.objects.filter(price__lt= 25)
    # data = Product.objects.filter(price__range= (80,83))
    
    # relation  -------------
    # data = Product.objects.filter(brand__id=5)
    # data = Product.objects.filter(brand__id__gt=200)
    
    # text  -------------
    # data = Product.objects.filter(name__contains='Bob')
    # data = Product.objects.filter(name__startswith='Bob')
    # data = Product.objects.filter(name__endswith='Thomas')
    # data = Product.objects.filter(price__isnull=True)
    
    # dates -------------
    # data = Product.objects.filter(date_column__year=2022)
    # data = Product.objects.filter(date_column__month=2)
    # data = Product.objects.filter(date_column__day=20)
    
    # complex queries -------------
    # data = Product.objects.filter(flag='New' , price__gt=98)
    # data = Product.objects.filter(flag='New').filter(price__gt=98)
    
    # data = Product.objects.filter(
    #     Q(flag='New') &
    #     Q(price__gt=98)
    #     )
    
    # data = Product.objects.filter(
    #     Q(flag='New') |
    #     Q(price__gt=98)
    #     )
    
    # data = Product.objects.filter(
    #     ~ Q(flag='New') |
    #     Q(price__gt=98)
    #     )
    
    # Field Refernce 
    # data = Product.objects.filter(quantity=F('price'))
    # data = Product.objects.filter(quantity=F('category__id'))
    
    # Order -------------
    # data = Product.objects.all().order_by('name')  # ASC
    # data = Product.objects.order_by('name')
    # data = Product.objects.order_by('-name')  # DES
    # data = Product.objects.order_by('-name','price')
    # data = Product.objects.filter(price__gt=80).order_by('name')
    # data = Product.objects.order_by('name')[:10]
    # data = Product.objects.earliest('name')
    # data = Product.objects.lates('name')
    
    # limit fields -------------
    # data = Product.objects.values('name','price')
    # data = Product.objects.values_list('name','price')
    # data = Product.objects.only('name','price')
    # data = Product.objects.defer('description','subtitle')
    
    # select related -------------
    # data = Product.objects.select_related('brand').all()   # ForiegnKey , One-to-one
    # data = Product.objects.prefetch_related('brand').all() # many-to-many
    # data = Product.objects.select_related('brand').select_related('category').all()
    
    # aggregation Count Min Max Sum AVG
    # data = Product.objects.aggregate(
    #     myavg =Avg('price'),
    #     mycount=Count('id')
    #     )
    
    # annotation 
    # data = Product.objects.annotate(is_new=Value(0))
    #data = Product.objects.annotate(price_with_tax=F('price')*1.15)
    
    data = Product.objects.all()

    return render(request,'products/debug.html',{'data':data})




# queryset : [products] : filter
# context : user

class ProductList(ListView):
    model = Product
    paginate_by = 50
    
    # show products with quantity only 
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(quantity__gt=0)
    #     return queryset
    
    
    
    
# context{} , queryset : Product.objects.all() : 1 : option   2 : method : overide
# querset : main query : detail product       
# context : extra data  : reviews , images
    
class ProductDetail(DetailView):    
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # dict : object product
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context['images'] = ProductImages.objects.filter(product=self.get_object())
        context['related'] = Product.objects.filter(brand=self.get_object().brand)
        return context
        
        
        
class BrandList(ListView):
    model = Brand
    paginate_by = 50
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
      
    
class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    paginate_by = 50
    
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])  # 5
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
        

    
# class BrandDetail(DetailView):
#     model = Brand
    
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.filter(brand=self.get_object())
#         return context
    
    
    
def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    
    review = request.POST['review']     # request.POST.get('review')  request.GET['review']  request.GET.get('review'])  
    rate = request.POST['rating']
    # add review
    
    Review.objects.create(
        user = request.user , 
        product = product , 
        review = review , 
        rate = rate
    )
    
    #return product_detail
    return redirect(f'/products/{slug}')