from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product_api.serializers.productSerializer import ProductSerializer
from product_api.models.product import Product


class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = self.serializer_class(product, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(status.HTTP_400_BAD_REQUEST)


class DetailProductView(APIView):
    serializer_class = ProductSerializer
    product = Product.objects

    def get(self, request, pk: int, format=None):
        serializer = self.serializer_class(self.product.get(pk=pk), many=False)
        return Response(serializer.data)

    def patch(self, request, pk: int):
        serializer = self.serializer_class(self.product.get(pk=pk), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        serializer = self.serializer_class(self.product.get(pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

