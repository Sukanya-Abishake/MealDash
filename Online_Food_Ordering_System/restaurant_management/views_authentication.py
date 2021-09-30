from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
import json
from .models import Restaurant
from .serializers import RestaurantSerializer
import requests


@api_view(['POST'])
def restaurant_register(request):
    if request.method == 'POST':
        restaurant_email = request.data['email']
        serializer = RestaurantSerializer(data=request.data)
        if restaurant_email is not None:
            restaurants = Restaurant.objects.all()
            restaurant = restaurants.filter(email__icontains=restaurant_email)
            if len(restaurant) == 0:
                if serializer.is_valid():
                    serializer.save()
                    r = requests.post(
                        'http://localhost:7000/notification/user/' + request.data['email'],
                        data={
                            'type': 'REGISTRATION',
                            'recipient': request.data['email']
                        }, params=request.POST)
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                print('Errors', serializer.errors)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'Restaurant already exists!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'Check the registration details again!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def restaurant_login(request):
    print(request);
    if request.method == 'POST':
        restaurant_data = JSONParser().parse(request)
        restaurant_email = restaurant_data['email']
        restaurant_password = restaurant_data['password']
        print(restaurant_email, restaurant_password)
        if restaurant_email is not None and restaurant_password is not None:
            # TODO - password hashing
            restaurants = Restaurant.objects.all()
            restaurant = restaurants.filter(email__icontains=restaurant_email)
            restaurant = restaurant.filter(password__icontains=restaurant_password)
            if (len(restaurant) != 0):
                serializer = RestaurantSerializer(restaurant, many=True)
                return JsonResponse(serializer.data[0], safe=False)
            else:
                return JsonResponse({'message': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)
