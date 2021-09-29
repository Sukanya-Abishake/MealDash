from rest_framework import serializers
from .models import Restaurant, Order, MealPlan, MealPlanItem
from .models import Item


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'password', 'email', 'address', 'latitude', 'longitude', 'phone', 'timestamp']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'description', 'price', 'start_time', 'end_time', 'status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'actual_price', 'customer', 'mealplan']


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ['id', 'description', 'actual_price', 'final_price', 'type', 'status']


class MealPlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlanItem
        fields = ['quantity']


class MealPlanItemDetailsSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False, read_only=False)

    class Meta:
        model = MealPlanItem
        fields = ['quantity', 'item']


class MealPlanDetailSerializer(serializers.ModelSerializer):
    mealPlanItems = MealPlanItemDetailsSerializer(many=True, read_only=False)

    class Meta:
        model = MealPlan
        fields = ['id', 'description', 'actual_price', 'final_price', 'type', 'status', 'mealPlanItems']
