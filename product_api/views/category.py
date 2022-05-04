from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product_api.serializers.categorySerializer import CategorySerializer
from product_api.models.category import Category


class CategoryView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = self.serializer_class(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(status.HTTP_400_BAD_REQUEST)


class DetailCategoryView(APIView):
    serializer_class = CategorySerializer
    category = Category.objects

    def get(self, request, pk: int, format=None) -> Response:
        serializer = self.serializer_class(self.category.get(pk=pk), many=False)
        return Response(serializer.data)

    def patch(self, request, pk: int) -> Response:
        serializer = self.serializer_class(self.category.get(pk=pk), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int) -> Response:
        serializer = self.serializer_class(self.category.get(pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, pk: int) -> Response:
        self.category.get(pk=pk).delete()
        return Response(status.HTTP_200_OK)
