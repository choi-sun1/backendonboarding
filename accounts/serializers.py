from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'nickname')

    def validate_password(self, value):
        """비밀번호 강도 검사를 추가"""
        try:
            validate_password(value)  # Django의 기본 비밀번호 검증 사용
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
    def create(self, validated_data):
        """유저 생성 시 비밀번호를 안전하게 저장"""
        user = CustomUser(
            username=validated_data["username"],
            nickname=validated_data["nickname"]
        )
        user.set_password(validated_data["password"])  # set_password() 사용
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username  # 토큰에 추가할 데이터
        return token