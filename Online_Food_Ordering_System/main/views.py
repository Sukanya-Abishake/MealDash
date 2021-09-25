from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import Product,CartItems
from main.serializers import ProductSerializer,CartItemsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.views import APIView

#Product
#CartItems

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemsList(generics.ListCreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer


class CartItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
