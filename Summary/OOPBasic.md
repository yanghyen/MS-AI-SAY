# Part2 : Object Oriented Programming (OOP, 객체지향 프로그래밍)
- 소스로 real world 묘사
- 객체 : 실생활에 존재하는 것들 (실존 안 하는 추상적인 것)
- 객체를 만들기 위해선 클래스 필요
- other PL : 1 class = 1 file
    - JAVA : 파일(.java) 자체가 class
- Python : 맘대로
    - 파일(.py)은 모듈, 모듈 속에 class 배치

### 변수명 규칙
- 변수명 : 소문자로 시작
- 클래스명 : 대문자로 시작

### Class
- class : 객체 찍는 도장/붕어빵 틀
- object/instance : 찍어낸 것/붕어빵
- member ~ : class 내 ~
    - member variable : 클래스 내 변수. 객체의 속성
    - method : 객체의 액션. 프로그램 상 필요한 기능 구현. member function은 없는 말!
- 변수
    - 전역변수 : 그냥 밖에 있는 거. global만 붙이면 아무데서나 다 쓸 수 있음
    - 지역변수 : 함수 속에서 만들어진 거. 그 함수 속에서만 사용 가능 => 함수 진행하는 동안만 쓰고 버림(임시)
    - 멤버변수(member variable, attribute, field) : 객체의 속성
- 함수(function) vs 메소드(method)
    - 함수 : 기능 모아놓은 것
    - 메소드 : 객체의 액션