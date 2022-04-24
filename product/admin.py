from django.contrib import admin
from .models import Product, ProductBrnd, ProductCategory, ProductPrice

admin.site.register(Product)
admin.site.register(ProductBrnd)
admin.site.register(ProductCategory)
admin.site.register(ProductPrice)