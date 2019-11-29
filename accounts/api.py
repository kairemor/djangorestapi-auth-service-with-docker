from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser
from knox.models import AuthToken
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.db.models import Q

from accounts.models import Department
from accounts.serializers import DepartmentSerializer
from internship.models import Enterprise, Convention


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    parser_class = (FileUploadParser,)
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            User.objects.get(email=email)
            return Response({
                "error": "email deja utilise"
            })
        except:
            pass
        user = serializer.save()
        user.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        print((request.data))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UsersAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()


class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user
