from django.contrib import admin
from .models import Product,CartItems

# Register your models here.

#Product
#CartItems
admin.site.register(Product)
admin.site.register(CartItems)