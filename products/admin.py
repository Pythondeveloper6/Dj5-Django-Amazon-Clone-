from django.contrib import admin
from .models import Product , Brand , Review , ProductImages


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]





admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)