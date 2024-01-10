from django.contrib import admin

# Register your models here.
from .models import Settings , DeliveryFee


admin.site.register(Settings)
admin.site.register(DeliveryFee)