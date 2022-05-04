from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from user_api.serializers import SupplierSerializer
from user_api.models import Suppliers


class SupplierApiView(APIView):
    """API View of User"""
    serializer_class = SupplierSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """GET Method to SupplierApiView"""
        supplier = Suppliers.objects.all()
        serializer = self.serializer_class(supplier, many=True)
        return Response(serializer.data)

    def post(self, request):
        """POST Method to SupplierApiView"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierDetailView(APIView):

    serializer_class = SupplierSerializer
    # permission_classes = [IsAuthenticated]
    supplier = Suppliers.objects

    def get(self, request, pk=None, *args, **kwargs):
        """GET Method to SupplierDetailView"""
        serializer = self.serializer_class(self.supplier.get(pk=pk), many=False)
        return Response(serializer.data)

    def put(self, request, pk=None):
        """PUT Method to SupplierDetailView"""
        serializer = self.serializer_class(self.supplier.get(pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """PATCH Method to SupplierDetailView"""
        serializer = self.serializer_class(self.supplier.get(pk=pk), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """DELETE Method to SupplierDetailView"""
        self.supplier.get(pk=pk).delete()
        return Response(f'id:{pk} deleted', status.HTTP_200_OK)
