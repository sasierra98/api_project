from rest_framework import serializers
from user_api.models import User


class UserSerializer(serializers.ModelSerializer):
    """Class to serializer user model"""
    # name = serializers.CharField(
    #     max_length=255,
    # )
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'email', 'identification', 'phone', 'cellphone', 'address', 'country', 'genre',
                  'is_active', 'is_staff', 'is_customer')
        