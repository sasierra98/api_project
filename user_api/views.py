from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from user_api.serializers import UserSerializer
from user_api.models import User


class UserApiView(APIView):
    """API View of User"""
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """GET Method to UserApiView"""
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        """POST Method to UserApiView"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # name = serializer.validated_data.get('name') #if use serializer.Serializer
            # message = f'Hello {name}'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # User.objects.make_random_password()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    user = User.objects

    def get(self, request, pk=None, *args, **kwargs):
        """GET Method to UserDetailView"""
        serializer = self.serializer_class(self.user.get(pk=pk), many=False)
        return Response(serializer.data)

    def put(self, request, pk=None):
        """PUT Method to UserDetailView"""
        serializer = self.serializer_class(self.user.get(pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """PATCH Method to UserDetailView"""
        serializer = self.serializer_class(self.user.get(pk=pk), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(f'{request.data} Updated', status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """DELETE Method to UserDetailView"""
        self.user.get(pk=pk).delete()
        return Response(f'id:{pk} deleted', status.HTTP_200_OK)
