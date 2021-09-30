from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
import json
from .models import Customer
from .serializers import CustomerSerializer


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        new_customer_data = JSONParser().parse(request)
        customer_email = new_customer_data['email']
        if customer_email is not None:
            customers = Customer.objects.all()
            customer = customers.filter(email__icontains=customer_email)
            if (len(customer) == 0):
                serializer = None
                serializer = CustomerSerializer(data=new_customer_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'Customer already exists!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'Check the registration details again!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_email = customer_data['email']
        customer_password = customer_data['password']
        print(customer_email, customer_password)
        if customer_email is not None and customer_password is not None:
            # TODO - password hashing
            customers = Customer.objects.all()
            customer = customers.filter(email__icontains=customer_email)
            customer = customers.filter(password__icontains=customer_password)
            if (len(customer) != 0):
                serializer = CustomerSerializer(customer, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({'message': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)
