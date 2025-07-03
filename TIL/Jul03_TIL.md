# 250703
## ✅TO-DO
### Remoria
- ✅다인언니 코랩 코드 인수인계(환경세팅, 논문 구조 바탕 설명)
- ✅스토리 에이전트 프롬프트 수정
    - ```ipdb.set_trace()``` 찍어두고 반환값 확인하면서 수정하기
### 블로그
- 리눅스 서버 -> 구글 드라이브 자료 보내는 글 
### Algorithm
- 스택 구조 공부 끝내기

## 📌Today I Learned
### ipdb 디버깅 방법
- 변수명을 입력하면 그 변수값을 알려준다. 에러 뜰 때 상관있는 변수들이 어떤 값을 갖는 지 확인한다. 그러다보면 False인 값을 찾게 되면, 그 값이 쓰이는 함수를 찾아가면 어디가 문제인지 알게된다.

## 💡 회고 / 인사이트
### ai가 준 코드 냅다 복붙 금지 !!!

## 💥 트러블슈팅
### 프롬프트 수정할 때 output format을 잘 맞춰야 한다. 
- gpt한테 프롬프트 써달라고 하면 맘대로 output format에 요소를 추가한다. asker랑 expert output format은 수정했는데, outline 파트 프롬프트는 수정 안 해서 outline이 생성되지 않았다. 왜냐면 outline은 json_parse_outline()에서 JSON 형식이 맞는지 체크한 뒤에 생성이 되는데, 그 함수에서 지정한 형식과 달라서 False를 반환했다. 계속 False를 반환해서 llm에 계속 요청 보내니까 max_try 값보다 더 많이 요청해서 openai key error가 떴다.
- outline write 관련 프롬프트 output format 수정했더니 해결 완
            
## 🍩내일 할 일
### Remoria
- 스토리 에이전트 프롬프트 수정
    - 줄거리랑 지역 정보 제공하고 요약해서 스토리 만드는 형식으로
- tmux 사용법 찾아보기
### 블로그
- 리눅스 서버 -> 구글 드라이브 자료 보내는 글 
### Algorithm
- 스택 구조 공부 끝내기