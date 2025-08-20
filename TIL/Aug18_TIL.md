# 250818-20
## ✅TO-DO
### Remoria
- 문화재 이미지 모델 학습
    1. 데이터셋 구축
    - ✅공공데이터 API에서 데이터 받아오기 (image_api2.py)
    - ✅name에서 지역, 시공 날짜 지우기
    - ✅gemini로 caption 영어로 번역
        - ✅gemini 설치
    2. ✅데이터셋 허깅페이스에 업로드 (dataset_compose2.py)
    3. ✅모델 학습
    4. ✅테스트 (inference.py)
### AI
- building effective agents에서 소개한 agent 구조들 정리
- positional encoding 블로그 정리
### 이력서
- 이력서 수정

## 📌Today I Learned
### 간단한 파일 전송은 runpodctl
- docker 컨테이너 내 파일은 filezilla나 여러 로컬 방식으로는 불가능하다. 이럴 때 rclone을 주로 쓴다고 

## 💡 회고 / 인사이트

## 💥 트러블슈팅
### 파인튜닝에서 중요한 것은 데이터셋 구축 !!!
- 문화유산 이미지로 파인튜닝한 결과가 마음에 들지 않는다.

### ```No space left on device```
- 파인튜닝 과정에서 계속 메모리 부족이 발목을 잡는다. 모델이랑 데이터셋을 다운받을 때 용량이 많이 든다. 그런데 이전에 사용하던 캐시 저장 공간도 비우고, 노트북 메모리도 정리했는데도 문제가 됐다. 


## 🍩내일 할 일