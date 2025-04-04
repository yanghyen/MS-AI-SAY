# Aspect Oriented Programmin (AOP, 관점지향프로그래밍) 
- Procedural Programming : 절차지향프로그래밍 -> OOP -> AOP
- 메소드들 공통된 부분들 정리하자
```py
 def ready(self):
    print("씻고 옷 입고")
    print("나가서 엘베 타고 내려가")

def goSchool(self):
    self.ready()
    print("버스 타고 학교로")

def goMart(self):
    self.ready()
    print("걸어서 마트로")

def goPark(self):
    self.ready()
    print("자전거 빌려서 공원으로")
```
### MVC 패턴
- 파일을 나누고, 한 파일은 한 명이 책임지고 끝내자
- Model : 비즈니스 로직(실제 계산)
- View : 실제로 사용자 눈에 보이는 입력받고, 결과 출력
    - FE, designer
- Controller : 상황 판단해서 M 필요하면 M 소환, V 필요하면 V 소환
    - 프로그램의 진입점