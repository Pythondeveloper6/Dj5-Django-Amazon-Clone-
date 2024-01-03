from rest_framework import serializers
from taggit.serializers import TagListSerializerField,TaggitSerializer
from .models import Product , Brand , ProductImages , Review


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']


class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user','review','rate','created_at']



class ProductListSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()
    
    class Meta:
        model = Product
        fields = ['name','price','flag','image','subtitle','description','sku','brand','review_count','avg_rate','tags']
                
        
        
class ProductDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    images = ProductImagesSerializer(source='product_image',many=True)
    reviews = ProductReviewsSerializer(source='review_product',many=True)
    tags = TagListSerializerField()
    
    class Meta:
        model = Product
        fields = ['name','price','flag','image','subtitle','description','sku','brand','review_count','avg_rate','images','reviews','tags']
        
        
        
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
        
class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
        