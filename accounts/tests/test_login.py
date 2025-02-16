import pytest
from accounts.models import CustomUser  # CustomUser 모델을 import
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_login():
    client = APIClient()

    # 회원가입 데이터 (로그인 전 미리 회원가입을 진행)
    signup_data = {
        "username": "JINHO",
        "password": "12341234",
        "nickname": "Mentos"
    }

    # 회원가입 요청
    signup_response = client.post("/api/signup/", signup_data, format='json')
    assert signup_response.status_code == 201  # 회원가입 성공 확인

    # CustomUser로 확인
    assert CustomUser.objects.filter(username="JINHO").exists()  # 유저 존재 확인

    # 로그인 데이터
    login_data = {
        "username": "JINHO",
        "password": "12341234"
    }

    # 로그인 요청
    response = client.post("/api/login/", login_data, format='json')

    # 응답 상태 코드 확인
    assert response.status_code == status.HTTP_200_OK