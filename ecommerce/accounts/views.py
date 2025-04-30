from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
import json
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


def register_page(request):
    return render(request, "register.html")


def login_page(request):
    return render(request, "login.html")


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = []

    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)
        email = request.data.get('email')
        user = authenticate(email=email, password=request.data.get('password'))

        if user:
            user_data = UserSerializer(user).data
            return Response({
                "access": response.data['access'],
                "refresh": response.data['refresh'],
                "user": json.dumps(user_data)
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
