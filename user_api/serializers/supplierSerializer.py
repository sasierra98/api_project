from rest_framework import serializers
from user_api.models import Suppliers


class SupplierSerializer(serializers.ModelSerializer):
    """Class to serializer suppliers model"""

    class Meta:
        model = Suppliers
        fields = '__all__'
