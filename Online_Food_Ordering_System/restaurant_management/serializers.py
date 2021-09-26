from rest_framework import serializers
from .models import Restaurant
from .models import Item


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'password', 'email', 'address', 'latitude', 'longitude', 'phone', 'timestamp']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'description', 'price', 'start_time', 'end_time', 'status', 'restaurant']

