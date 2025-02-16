from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class SignupView(APIView):
    permission_classes = []
    authentication_classes = []

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
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class MyTokenObtainPairView(TokenObtainPairView):
    def get_serializer_class(self):
        from .serializers import MyTokenObtainPairSerializer  
        return MyTokenObtainPairSerializer

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = RefreshToken(refresh_token)
            return Response({'access_token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProtectedEndpointView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You have access to this protected endpoint!"})