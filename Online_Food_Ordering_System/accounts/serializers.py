from rest_framework import serializers
from accounts.models import Customer
 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'address', 'pincode','password']

