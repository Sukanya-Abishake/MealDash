"""Online_Food_Ordering_System URL Configuration

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
from main import views

urlpatterns = [
    path('api/core/product/', views.ProductList.as_view())  ,
    path('api/core/product/<int:pk>/', views.ProductDetail.as_view())  ,
    path('api/core/cartItems/', views.CartItemsList.as_view())  ,
    path('api/core/cartItems/<int:pk>/', views.CartItemsDetail.as_view())  ,
]
