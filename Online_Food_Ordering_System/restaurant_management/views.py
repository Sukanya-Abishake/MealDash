from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Order, MealPlan
from .models import Item
from .serializers import RestaurantSerializer, OrderSerializer, MealPlanSerializer
from .serializers import ItemSerializer
from rest_framework import generics, status


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = RestaurantSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class MealPlanList(generics.ListCreateAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class MealPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class RestaurantAPIView(APIView):
    def get(self, request, restaurantId):
        print('Restaurant:Id:', restaurantId)
        try:
            item_query_set = Item.objects.filter(restaurant_id= restaurantId)
            print('queryset', item_query_set)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item_query_set, many=True)
        print('Serializer', serializer)
        return Response(serializer.data)
