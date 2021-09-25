from rest_framework import serializers
from main.models import Product
from main.models import CartItems

#Product
#CartItems
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'instructions', 'image','created_by']

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'item', 'ordered', 'quantity', 'ordered_date', 'status','delivery_date','customer']


