from django.contrib import admin

from .models import Restaurant, MealPlan, Order
from .models import Item

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(MealPlan)
admin.site.register(Order)


