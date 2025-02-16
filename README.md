# backendonboarding

## Requirements

- [x] Pytest를 이용한 테스트 코드 작성법 이해
- [x] Django를 이용한 인증과 권한 이해
- [x] JWT와 구체적인 알고리즘의 이해
- [x] PR 날려보기
- [x] 리뷰 바탕으로 개선하기
- [x] EC2에 배포해보기

### 시나리오 설계 및 코딩 시작!

#### Django 기본 이해

- [x] Middleware란 무엇인가? (with Decorators)
- [x] Django란?

#### JWT 기본 이해

- [x] JWT란 무엇인가요?

### 시나리오 설계 및 코딩 시작!

#### 토큰 발행과 유효성 확인

- [x] Access / Refresh Token 발행과 검증에 관한 테스트 시나리오 작성하기

#### 유닛 테스트 작성

- [x] Pytest를 이용한 JWT Unit 테스트 코드 작성해보기

### 백엔드 배포하기

#### 테스트 완성

- [x] 백엔드 유닛 테스트 완성하기

#### 로직 작성

- [x] 백엔드 로직을 Django로 작성
  - [x] 회원가입 - `/signup`
    - **Request Message**

      ```json
      {
        "username": "JIN HO",
        "password": "12341234",
        "nickname": "Mentos"
      }
      ```

    - **Response Message**

      ```json
      {
        "username": "JIN HO",
        "nickname": "Mentos",
        "roles": [
          {
            "role": "USER"
          }
        ]
      }
      ```

  - [x] 로그인 - `/login`
    - **Request Message**

      ```json
      {
        "username": "JIN HO",
        "password": "12341234"
      }
      ```

    - **Response Message**

      ```json
      {
        "token": "eKDIkdfjoakIdkfjpekdkcjdkoIOdjOKJDFOlLDKFJKL"
      }
      ```

### 백엔드 배포하고 개선하기

#### 배포해보기

- [x] AWS EC2에 배포하기

#### API 접근과 검증

- [x] Swagger UI로 접속 가능하게 하기

[Git 커밋 메시지 잘 쓰는 법 | GeekNews](https://news.hada.io/topic?id=9178&utm_source=slack&utm_medium=bot&utm_campaign=TQ595477U)

#### AI-assisted programming

- [x] AI에게 코드리뷰 받아보기

#### Refactoring

- [x] 피드백 받아서 코드 개선하기

#### 마무리

- [x] AWS EC2 재배포하기
