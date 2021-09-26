"""Meal_Dash_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import views_authentication

urlpatterns = [
    path('api/authentication/restaurant/registration/', views_authentication.restaurant_register),
    path('api/authentication/restaurant/login/', views_authentication.restaurant_login),
    path('api/core/getRestaurantList/', views.RestaurantList.as_view()),
    path('api/core/getRestaurantDetail/<int:pk>/', views.RestaurantDetail.as_view()),
    path('api/core/getItemList/', views.ItemList.as_view()),
    path('api/core/getItemDetail/<int:pk>/', views.ItemDetail.as_view()),
    path('api/core/getMealPlanList/', views.MealPlanList.as_view()),
    path('api/core/getMealPlanDetail/<int:pk>/', views.MealPlanDetail.as_view()),
    path('api/core/getOrderList/', views.OrderList.as_view()),
    path('api/core/getOrderDetail/<int:pk>/', views.OrderDetail.as_view()),
]
