from django.urls import path
from .views import SignupView,LoginView, RefreshTokenView, MyTokenObtainPairView, ProtectedEndpointView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT 토큰 발급
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),   # JWT 토큰 갱신
    path('protected-endpoint/', views.ProtectedEndpointView.as_view(), name='protected-endpoint'),
]