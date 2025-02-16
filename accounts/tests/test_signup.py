import pytest
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_signup():
    client = APIClient()

    # 회원가입을 위한 데이터
    signup_data = {
        "username": "JINHO",
        "password": "12341234",
        "nickname": "Mentos"
    }

    # POST 요청 보내기
    response = client.post("/api/signup/", signup_data, format='json')

    # 응답 상태 코드 확인
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_login():
    client = APIClient()

    # 로그인 데이터
    login_data = {
        "username": "JINHO",
        "password": "12341234"
    }

    # 로그인 요청
    response = client.post("/api/login/", login_data, format='json')

    # 응답 상태 코드 확인
    assert response.status_code == status.HTTP_200_OK

    # 응답 내용 확인 (예: token이 포함되었는지 확인)
    assert "token" in response.data