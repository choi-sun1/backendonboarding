from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname')

    def validate(self, attrs):
        """비밀번호 강도 검사를 추가"""
        password = attrs.get("password")
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        return super().validate(attrs)

    def create(self, validated_data):
        """유저 생성 시 비밀번호를 안전하게 저장"""
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])  # 비밀번호 해싱
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["nickname"] = user.nickname  # 닉네임도 토큰에 포함
        return token