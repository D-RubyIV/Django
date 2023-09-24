import datetime
from rest_framework import serializers
from .models import Product, Customer
from dataclasses import fields
from rest_framework import serializers
from .models import Customer,Product
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
        
        


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token["password"] = user.password

        return token
    
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'