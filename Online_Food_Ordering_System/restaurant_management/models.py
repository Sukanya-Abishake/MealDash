from django.db import models

# Create your models here.
from user_management.models import Customer


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


class MealPlan(models.Model):
    MEAL_PLAN_TYPE = (
        ('custom', 'Custom'),
        ('default', 'Default')
    )
    description = models.CharField(max_length=120)
    actual_price = models.FloatField(max_length=15)
    final_price = models.FloatField(max_length=15)
    type = models.CharField(max_length=15, choices=MEAL_PLAN_TYPE, default='default')
    status = models.CharField(max_length=15)
    restaurant = models.ForeignKey(Restaurant, related_name='meal_plan', on_delete=models.CASCADE)


class MealPlanItem(models.Model):
    mealPlan = models.ForeignKey(MealPlan, related_name='mealPlanItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='mealPlanItems', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    status = models.CharField(max_length=120)
    actual_price = models.FloatField(max_length=15)
    customer = models.ForeignKey(Customer, related_name='custmer_item', on_delete=models.CASCADE)
    mealplan = models.ForeignKey(MealPlan, related_name='mealplan_item', on_delete=models.CASCADE)
