# 250724
## ✅TO-DO
### Remoria
- ✅reference image prompt wrtier 구현
    - ✅output form 영어로 바꾸고 프롬프트 잘 나오는지 확인
- ✅meta writer 구현 
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리

## 📌Today I Learned
### 문제 원인 파악이 문제 해결의 첫 단계!
- 에러 메세지를 보고 디버깅을 통해 해결 방법을 모색하면 된다.

### 프롬프트의 중요성
- 프롬프트 작성이 중요하다고는 들었는데 이렇게까지 영향이 큰줄은 몰랐다. 또 전달받은 meta data write 프롬프트는 바로 형식에 맞게 전달돼서 약간 허탈하다. 내 프롬프트랑 비교하면서 뭐가 다른지 살펴보자.

## 💡 회고 / 인사이트
### 모델 별 특징 파악의 필요성
- gpt api에게 json 포맷을 요청한 뒤 응답을 받으면, api 응답이 text로 오기 때문에 이스케이프 처리된 문자열로 받게 된다. 그러면 디코딩하는 과정이 필요하다. 
- 이런 식으로 모델마다 각각의 특징이 있어서 파악할 필요성이 있다. 

## 💥 트러블슈팅
### rule base 가능 여부를 항상 염두에 둘 것.
- 이틀 간 레퍼런스 이미지 프롬프트 생성 에이전트 구현했는데, 결국은 rule base로 진행하기로 했다. 이렇게 하니까 정말 30분만에 내가 그토록 원하던 형식의 프롬프트가 생성됐다. ㅋㅋㅋ 불필요한 llm 호출이 얼마나 비효율적인지 여실히 깨닫게 됐다.

## 🍩내일 할 일
- 트러블슈팅(2) 마무리
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리