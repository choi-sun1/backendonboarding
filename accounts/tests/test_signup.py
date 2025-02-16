import pytest
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_signup():
    client = APIClient()

    # 회원가입 데이터
    signup_data = {
        "username": "JINHO",
        "password": "12341234",
        "nickname": "Mentos"
    }

    # 회원가입 요청
    response = client.post("/api/signup/", signup_data, format='json')

    # 응답 상태 코드 확인
    assert response.status_code == status.HTTP_201_CREATED

    # 응답 내용 확인
    response_data = response.json()
    assert response_data['username'] == signup_data['username']
    assert response_data['nickname'] == signup_data['nickname']
    assert 'roles' in response_data
    assert len(response_data['roles']) > 0
