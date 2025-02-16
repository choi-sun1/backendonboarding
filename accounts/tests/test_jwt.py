import pytest
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestJWT:

    @pytest.fixture
    def user_data(self):
        return {
            "username": "JINHO",
            "password": "12341234",
            "nickname": "Mentos"
        }

    @pytest.fixture
    def client(self):
        return APIClient()

    # 회원가입 후 로그인하여 JWT 토큰 발급 확인
    def test_signup_and_login(self, client, user_data):
        # 올바른 회원가입 URL로 변경
        signup_response = client.post('/api/signup/', user_data, format='json')
        assert signup_response.status_code == status.HTTP_201_CREATED, f"Expected 201, got {signup_response.status_code}"
        
        # 로그인 요청
        login_data = {
            'username': user_data['username'],
            'password': user_data['password']
        }
        login_response = client.post('/api/login/', login_data, format='json')
        
        assert login_response.status_code == status.HTTP_200_OK, f"Login failed, got {login_response.status_code}"
        assert 'access_token' in login_response.data
        assert 'refresh_token' in login_response.data

    # JWT가 유효한지 확인하는 테스트
    def test_jwt_access(self, client, user_data):
        client.post('/api/signup/', user_data, format='json')
        login_data = {
            'username': user_data['username'],
            'password': user_data['password']
        }
        login_response = client.post('/api/login/', login_data, format='json')
        access_token = login_response.data['access_token']  # 'access_token' 정확한 키 이름으로 수정
        
        # JWT 토큰을 Authorization 헤더에 포함하여 인증된 API 호출
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = client.get('/api/protected-endpoint/')  
        
        assert response.status_code == status.HTTP_200_OK, f"Expected 200, got {response.status_code}"

    # 잘못된 JWT 토큰 처리
    def test_invalid_jwt(self, client):
        client.credentials(HTTP_AUTHORIZATION='Bearer invalidtoken')
        response = client.get('/api/protected-endpoint/')  # 경로 수정
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED, f"Expected 401, got {response.status_code}"