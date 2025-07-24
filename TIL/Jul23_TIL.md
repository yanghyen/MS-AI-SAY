# 250723
## ✅TO-DO
### Remoria
- reference image prompt wrtier 구현
- meta writer 구현 
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리


## 📌Today I Learned

## 💡 회고 / 인사이트

## 💥 트러블슈팅
### 에러 메세지가 뜨지 않는 문제가 생겼을 때, 문제의 원인을 생각해보자.
- 이상하게 이미지 생성이 안되는 프롬프트가 있었다. 저작권에 걸리는 내용은 생성이 안된다고 한다. 에러 메세지가 떴으면 좋았겠지만,, 생성되지 않는 상황에서 원인을 찾기보다 무작정 계속 모델을 돌린 건 비효율적이다. 

### 시야를 넓히자,,
- ref img prompt를 생성하는 과정에서 승환이가 작성했던 프롬프트를 레퍼런스로 삼았다. flux 모델에 적합한 기준을 잡고 진행한 시도는 좋았지만, 잘 되지 않으면 다른 방안도 생각할 수 있어야 한다. 프롬프트가 output form에 잘 맞춰서 줄글로 작성하지 못하면 json형식으로 output form을 잡고, json 형식 처리 메소드를 구현하면 된다.
- 백엔드 개발을 하며 생긴 경험을 AI에도 적용할 수 있어야 한다. 

### 코드를 파악하고 생각하고 실행하자
- scene_text.json 파일을 불러와서 내 로직들이 실행됐다. 그럼 해당 파일을 불러오기 이전의 코드들은 굳이 실행되지 않아도 되는데, 코드를 파악하지 않아서 하염없이 기다렸다. 시간을 많이도 날렸다.

## 🍩내일 할 일
### Remoria
- reference image prompt wrtier 구현
- meta writer 구현 
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리