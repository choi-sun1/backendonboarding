from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class SignupView(APIView):
    permission_classes = [] 
    def post(self, request):
        from .serializers import SignupSerializer  
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username": user.username,
                "nickname": user.nickname,
                "roles": [{"role": "USER"}]
            }, status=status.HTTP_201_CREATED)
        else:
            # serializer.errors를 출력하여 어떤 오류가 발생했는지 확인
            print(serializer.errors)  # 콘솔에 출력
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                # JWT 토큰 생성
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # 로그인 성공 시 응답에 JWT 토큰을 포함하여 반환
                return Response({
                    'access_token': access_token,
                    'refresh_token': str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'detail': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    def get_serializer_class(self):
        from .serializers import MyTokenObtainPairSerializer  
        return MyTokenObtainPairSerializer

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class RefreshTokenView(APIView):
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data['refresh_token']

            try:
                refresh = RefreshToken(refresh_token)
                access_token = str(refresh.access_token)

                return Response({'access_token': access_token}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)