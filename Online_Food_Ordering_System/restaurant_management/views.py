from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Order, MealPlan
from .models import Item
from .serializers import RestaurantSerializer, OrderSerializer, MealPlanSerializer, MealPlanItemSerializer, \
    MealPlanDetailSerializer
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

    def post(self, request,restaurantId):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            try:
                restaurant_query_set = Restaurant.objects.get(id = restaurantId)
            except Restaurant.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if serializer.is_valid():
                serializer.validated_data.__setitem__('restaurant', restaurant_query_set)
            serializer.save()
            #saved_course = Course.objects.get(courseId=serializer.data.get('courseId'))
            #self.email_students(request, CourseDetailSerializer(saved_course).data, "NEW_COURSE")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealPlanAPIView(APIView):
    def get(self, request, restaurantId):
        print('Restaurant:Id:', restaurantId)
        try:
            item_query_set = MealPlan.objects.filter(restaurant_id= restaurantId)
            print('queryset', item_query_set)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MealPlanSerializer(item_query_set, many=True)
        print('Serializer', serializer)
        return Response(serializer.data)

    def post(self, request,restaurantId):
        if request.data['type'] == 'custom':
            request.data['status'] = 'PENDING'
        serializer = MealPlanSerializer(data=request.data)
        if serializer.is_valid():
            try:
                restaurant_query_set = Restaurant.objects.get(id = restaurantId)
            except Restaurant.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if serializer.is_valid():
                serializer.validated_data.__setitem__('restaurant', restaurant_query_set)
            serializer.save()
            try:
                saved_meal_plan = MealPlan.objects.get(id=serializer.data['id'])
            except MealPlan.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in request.data['items']:
                print('Item: ',i)
                try:
                    item = Item.objects.get(id=i['itemId'])
                except Item.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                to_save_meal_plan_item = MealPlanItemSerializer(data=i)
                if to_save_meal_plan_item.is_valid():
                    print('Valid-MealPlanItem')
                    to_save_meal_plan_item.validated_data.__setitem__('mealPlan', saved_meal_plan)
                    to_save_meal_plan_item.validated_data.__setitem__('item', item)
                    to_save_meal_plan_item.save()
                else:
                    print('Not valid', to_save_meal_plan_item.errors)
            #saved_course = Course.objects.get(courseId=serializer.data.get('courseId'))
            #self.email_students(request, CourseDetailSerializer(saved_course).data, "NEW_COURSE")
            return Response(MealPlanDetailSerializer(saved_meal_plan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,restaurantId, mealPlanId):
        print("Patch", request.data)
        try:
            meal_plan = MealPlan.objects.get(id=mealPlanId)
        except MealPlan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print('Valid-MealPlanItem')
        meal_plan.status = request.data['status']
        meal_plan.save()
        return Response(MealPlanDetailSerializer(meal_plan).data, status=status.HTTP_201_CREATED)