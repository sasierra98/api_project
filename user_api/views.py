from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_api.serializers import UserSerializer
from user_api.models import User


class UserApiView(APIView):
    """API View of User"""
    serializer_class = UserSerializer

    def get(self, request, format=None):
        """Return a list of data from APIView"""
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # name = serializer.validated_data.get('name') #if use serializer.Serializer
            # message = f'Hello {name}'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request, pk=None):
    #     return Response({'method': 'PUT'})
    #
    # def patch(self, request, pk=None):
    #     return Response({'method': 'PATCH'})
    #
    # def delete(self, request, pk=None):
    #     return Response({'method': 'DELETE'})