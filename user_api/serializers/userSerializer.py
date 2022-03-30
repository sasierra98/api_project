from rest_framework import serializers
from user_api.models import User


class UserSerializer(serializers.ModelSerializer):
    """Class to serializer user model"""
    # name = serializers.CharField(
    #     max_length=255,
    # )
    class Meta:
        model = User
        fields = ['name', 'email', 'identification', 'phone', 'cellphone', 'address', 'country', 'genre']
