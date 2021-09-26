from django.contrib import admin

from .models import Restaurant
from .models import Item

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Item)


