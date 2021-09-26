from rest_framework import serializers
from user_management.models import Customer
 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'address', 'pincode','password']

