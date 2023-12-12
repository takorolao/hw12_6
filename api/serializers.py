from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product
from .models import User

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description','price']
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)