from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Item(models.Model):
    description = models.CharField(max_length=120)
    price = models.FloatField(max_length=15)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    restaurant = models.ForeignKey(Restaurant, related_name='items', on_delete=models.CASCADE)
