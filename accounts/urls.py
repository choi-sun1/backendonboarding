from django.urls import path
from .views import SignupView,LoginView, RefreshTokenView, MyTokenObtainPairView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),  # 회원가입
    path('login/', LoginView.as_view(), name='login'),      # 로그인
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT 토큰 발급
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),   # JWT 토큰 갱신
]