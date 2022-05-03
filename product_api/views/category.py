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