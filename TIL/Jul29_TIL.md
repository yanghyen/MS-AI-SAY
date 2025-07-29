# 250729
## ✅TO-DO
### Remoria
- ref img prompt 오류 찾기 
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리

## 📌Today I Learned

## 💡 회고 / 인사이트

## 💥 트러블슈팅
### 모델-백 연동 중 엔드포인트 에러
- 모델과 백을 연동하는 과정에서 계속 엔드포인트가 일치하지 않다는 에러가 떴다. 일치하는데!!! 알고 보니 ```app.include_router(router)```이 코드가 메소드 위에 위치해서 발생한 오류였다. 
- ```app.include_router(router)```는 라우트들을 FastAPI 앱에 연결하는 역할을 한다고 한다. 그동안 FastAPI를 배울 땐 간단한 프로젝트 기반이라 쓸 일이 없었는데, 프로젝트 규모가 커지면서 관리할 라우트가 많아서 사용하게 됐다. Django에서 urls.py 내 include("app.urls")로 라우트들을 관리했던 거랑 비슷한 것 같다.
## 🍩내일 할 일
### Remoria
- ref img prompt 오류 찾기 
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리