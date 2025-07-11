# 250710
## ✅TO-DO
- 이력서 작성
### Remoria
- Refine Writer Agent 구축
    - ✅VS로 돌려보기
    - ✅코드 공유 및 리뷰
- Auto Encoder 1번 강의 정리
- positional encoding 블로그 정리
- 스토리 에이트 프롬프트 수정 방법 정리
### Algorithm
- 스택 구조 공부 끝내기

## 📌Today I Learned
### Positional encoding
- 빠른 속도를 위해 병렬 처리를 도입한 Transformer에 발생한 문제점은 "단어의 순서" 정보가 상실된 것. 이를 해결하기 위해 도입한 게 positional encoding. 각 임베딩마다 순서 벡터를 더해준다. 이 순서 벡터는 여러 규칙에 의해 sine, cosine 함수로 도입하게 됐다.

## 💡 회고 / 인사이트
### 흐름을 수동적으로 이해하는 것보다 능동적으로 이해하며 논리를 완성해야 함
- 이 순서 벡터도 concatenate하느냐 summation하느냐 논의가 있었다. 단순히 차원 문제로 인해 summation을 선택한줄 알았는데, 두 방법의 과정을 계산하다보면 summation이 결국 concatenate의 정규화한 결과가 summation이란 얘기를 잠깐 들었다. 이건 다시 물어보고 정리해야겠다.
- LSTM이 디자인된 목적은 RNN의 기억력 감소 한계를 보완하기 위함 정도는 알았다. 그때 **RNN에 기억력 감소 한계가 왜 발생하는가**에 대해 생각해보라는 인사이트를 얻었다. RNN 구조를 살펴보면 각 레이어마다 같은 가중치 행렬을 곱한다. 그렇기 때문에 처음 데이터가 희미해진다. 
- 위 예시처럼 능동적인 질문을 던질줄 알아야 한다. 그럴 때 시야가 확장되는 것 같다. 논문을 읽을 때도 작성자의 시점으로 내용을 예측하며 읽고, 내 예측과 흐름이 다를 때 질문을 던져야 한다.

## 💥 트러블슈팅
### 라이브러리 버전 관리는 가상환경으로
- story agent를 테스트하는 과정에서 수정할 데이터가 많은데 일일이 리눅스에서 수정하기 번거로우니 VS code에서 수정해서 돌려봤다. 이때 로컬에는 이미 여러 라이브러리 설치가 돼있으니 venv 가상환경을 세팅해서 진행했다.
```py
# 가상환경 생성
python -m venv venv
# 가상환경 실행
.\venv\Scripts\activate
# requirements.txt 설치
pip install -r requirements.txt
```
## 🍩내일 할 일
- 이력서 작성
### Remoria
- Refine Writer Agent 구축
    - 여러 에이전트로 나눠보고, 처음에 어떤 도구를 선택할지 에이전트에게 선택권 줘보자
- Auto Encoder 1번 강의 정리
- positional encoding 블로그 정리
- 스토리 에이트 프롬프트 수정 방법 정리
### Algorithm
- 스택 구조 공부 끝내기