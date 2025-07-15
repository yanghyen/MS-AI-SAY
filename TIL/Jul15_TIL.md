# 250715
## ✅TO-DO
### AI
- ✅information Theory 블로그 읽기
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리
- ✅VAE 수식 이해
### Remoria
- 스토리 에이트 프롬프트 수정 방법 정리
- BE 코드 훑기
    - ✅디렉토리 구조 파악
    - 카카오 소셜 로그인 기능

## 📌Today I Learned
### information theory
- entropy란 최적의 전략 하에서 그 사건을 예측하는 데에 필요한 질문 개수, 필요한 질문개수에 대한 기댓값
- entropy가 감소한다는 건 그 사건을 맞히기 위해 필요한 질문의 개수가 줄어든다는 의미이자, 정보량이 줄어든다는 의미이다.
- 정보량을 수식화 하면 -logp(x), log를 취한 건 다음과 같은 이유 때문이다.
    1. 정보량은 확률이 낮을수록 커야 한다
    2. 독립 사건의 정보량은 합쳐져야 한다
    3. 정보량은 항상 0 이상, 연속적이며 단조 감소 함수
- 정보량의 기댓값이 엔트로피인데, E(-logp(x))를 전개하면 
    - H(p)=E_x∼p[I(x)]=−∑p(x)logp(x)
    - 엔트로피 감소는 예측 가능성이 증가한 상태 (정보가 더 있는 상태)
    - 불확실성 감소 = 정보 증가
- 크로스 엔트로피는 실제 분포는 p(x)인데, 모델이 예측하는 분포가 q(x)일 때 q(x)를 기반으로 정보 계산한 것
- −∑p(x)logq(x)
    - Cross Entropy는 "모델 q(x)가 예측한 값으로 코딩했을 때, 실제 데이터 p(x)를 얼마나 비효율적으로 표현하게 되는가?"
    - 정확한 예측일수록 Cross Entropy는 Entropy에 가까워짐
- KL Divergence는 우리가 모델 분포 q(x)를 사용함으로써 낭비되는 정보량(비효율성)
    - ∑p(x)log(q(x)/p(x))
​
### VAE
- 단순한 압축이 아니라, 확률적 latent space를 학습해서 새로운 데이터도 생성할 수 있도록 함
- 학습된 z 공간에서 샘플링해 새로운 x′ 생성 가능 → Generative Model
- 그래서 손실함수로 추적해야 하는 값이
    1. x'가 x와 얼마나 비슷하냐 - reconstruction loss(cross entropy로 나타냄)
    2. z가 얼마나 정규분포와 비슷하냐 - KL Divergence
    - 이때 logp(x)를 직접 계산할 수 없어서 우리가 계산할 수 있는 하한선인 ELBO를 구해서 
    - ELBO를 최대화하여 간접적으로 logp(X)도 커지게 하는 것
    - 최종 손실 함수는 ELBO(Evidence Lower Bound)의 음수
    - Loss = −ELBO = −E[logp(x∣z)] + D_KL(q(z∣x)∥p(z))

### SQLAlchemy
- SQLAlchemy는 파이썬에서 데이터베이스를 쉽게 다룰 수 있게 해주는 라이브러리
- jpa 같은 존재
- refresh()
    - commit()해서 DB에 반영된 데이터를 다시 SELECT해서 객체를 최신 상태로 동기화
    - commit()만 하면 트랜잭션이 DB에 반영 안될 수 있음
| 메서드               | 역할                                   |
| ----------------- | ------------------------------------ |
| `db.commit()`     | DB에 트랜잭션을 확정하고 저장                    |
| `db.refresh(obj)` | 해당 객체의 값을 **DB에서 다시 불러와 최신 상태로 동기화** |


## 💡 회고 / 인사이트

## 💥 트러블슈팅

## 🍩내일 할 일
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리
- story agent 서버 코드 수정해서 돌려보기
    1. summary/ meta data까지 구현
    2. data path 수정
    3. 서버 수정 작업
### Remoria
- 스토리 에이트 프롬프트 수정 방법 정리
- BE 코드 훑기
    - 카카오 소셜 로그인
    - 가이드 프로필 등록
### JAVA
- 자바의정석 CH1, 2 훑기