
from django.contrib import admin
from .models import Product, Seller

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'original_price', 'offer_price', 'seller')
    # Add any other fields you need

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'rating', 'warranty_offer')
    # Add any other fields you need
