# Python : 프로그래밍 언어
- 빅데이터 분석/훈련을 위해 LINUX, DB 다루는 건 당연티비
- 웹에서 훈련용 데이터 받아서 DB에 저장하고 Azure에서 실행하는 프로그램 만드는 게 목표 
- pip : Python에서 코드 공유 중앙제어시스템
```pip install 이름```

## python 프로그램 실행 명령어
```python
python 파일명
```

## 실행파일 만들기
1. Windos 용
- dos : 명령어 기반
- window : dos에 스킨 (클릭하면 명령어가 발동)
- .bat : 명령어 써놓은 파일 (win 용)
- p02_test2.bat 에 python p02_test2.py 라고 입력해둠 

2. Python 용
- pyinstaller : 실행 파일 만들어주는 라이브러리 
- pyinstaller는 PC에 Python 없어도 가능
- .bat는 PC에 Python 있어야 함
- 실행파일 경로 : ..\dist\p02_test

```py
# pyinstaller 설치
pip install pyinstaller

# 해당 파일 있는 경로 내
# C:Yang\workspace\Python\Mar04_1_Test
# 실행 파일 생성
pyinstaller 파일명
```
