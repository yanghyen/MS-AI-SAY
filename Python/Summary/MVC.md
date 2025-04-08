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
    - 
- View : 실제로 사용자 눈에 보이는 입력받고, 결과 출력
    - FE, designer
    - V가 웹사이트, 앱 화면,...
- Controller : 상황 판단해서 M 필요하면 M 소환, V 필요하면 V 소환
    - 프로그램의 진입점 : HomeController, MainController

### DAO/DTO 패턴
- 기본 : MVC 패턴
- DAO(Data Access Object) : Model 중에 DB 관련 작업하는 파일
- DTO(Data Temp/Transfer Object) : M - V- C 간에 왔다갔다 하는 데이터 

### AOP와 MVC
- DB 작업마다 같은 작업 수행 => library로 만들자
