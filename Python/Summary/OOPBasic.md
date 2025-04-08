# Part2 : Object Oriented Programming (OOP, 객체지향 프로그래밍)
- 소스로 real world 묘사
- 객체 : 실생활에 존재하는 것들 (실존 안 하는 추상적인 것)
- 객체를 만들기 위해선 클래스 필요
- other PL : 1 class = 1 file
    - JAVA : 파일(.java) 자체가 class
- Python : 맘대로
    - 파일(.py)은 모듈, 모듈 속에 class 배치

## 변수명 규칙
- 변수명 : 소문자로 시작
- 클래스명 : 대문자로 시작

## Class
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

### method
- 액션/프로그램 상 필요한 기능
- 첫번째 파라미터로 self 무조건, 두번재부터는 마음대로 (문법)
- 호출할 때는 self 없는 셈 치셈
- 원래 Python에선
    ```Cat.meow(c1, 3)```처럼 썼다가 다른 PL처럼 쓸 수 있도록 허용해준 것
- constructor (생성자)
    - 객체 생성
        - 변수 = 클래스명() : 생성자 호출
    ```py
    class Phone:
        name = None
        manufacturer = None
        price = None

        # default constructor(기본 생성자)
        # 클래스에 생성자 작업 안 하면 Python이 자동으로 만들어서 씀
        def __init__(self):
            print("핸드폰 입고됨")

    hyeins = Phone() # 이때 호출됨
    ```
    - 생성자를 이용해서 객체 한번에 생성
    ```py
    class Computer:
        cpu = None
        ram = None
        hdd = None

        def __init__(self, c, ram, hdd):
            self.cpu = c    # c는 위에 cpu와 무관
            self.ram = ram
            self.hdd = hdd

    c = Computer("i5-1234", 16, 500)
    ```
- destructor(소멸자)
    - 객체가 없어질 때 작업
    ```py
     def __del__(self):
        print("빠잉")
    
    p3.showInfo()

    p2 = None       # p2의 stack이 사라져서 이때 GC 발동됨 => 빠잉 출력 
    print("hi")
    >>>
    빠잉
    hi
    빠잉
    ```

### static member variable
- 메모리의 static 영역에 만들어짐
- 메모리 절약 효과
- Python
    - 메모리 절약에 관심X
    - smv가 있긴 하지만 극적인 효과X

### static method
- 객체를 만들지 않고도 사용할 수 있는 메소드
- 객체는 언제 만드는가?
- 변수 : 데이터 임시 저장할 때
- 객체 : 데이터 실생활스럽게 임시 저장할 때
    - 저장이 필요하지 않으면 만들지 말아야 함!
- 생성 : self를 빼면 됨
- 호출 : 클래스명.메소드명(...)
    ```py
    class Calculator:
        @staticmethod  # 가독성 측면에서 부여 (옵션)
        def printSum(x, y):
            print(x + y)

    # static method 호출
    Calculator.printSum(10, 20)
    ```

### overloading
- overloading : 같은 이름의 메소드를 여러 개 정의하는 것.      
    - JAVA
        - 파라미터 다르면 함수명 같아도 됨 => 일부러 같게 
        - 생성자 다양하게 만들어두고, 필요한 것들 갖다 씀
    - Python
        - 구조상 overloading 불가능 = 생성자 하나만 가능
        - 생성자 여러개 만들어놓고 필요한 거 갖다쓰기 불가능

### Garbage Collection
- heap 영역 메모리 자동정리 시스템
- stack : 프로그램 종료시 자동 정리 (데이터 주소값)
- heap : 자동정리X, 개발자가 직접 정리 (데이터)
- GC 언제?
    - 그 번지를 더이상 사용하지 못하게 되면
    - 증명 : 그 번지를 가리키던 변수가 더이상 안 가리키게 되면
    - stack 영역이 정리되면 그에 해당하는 heap 영역 데이터도 못 쓰니까, 순차적으로 heap도 정리됨
    ```py
    # p2의 stack이 사라져서 이때 GC 발동됨 => 빠잉 출력 
    p2 = None        
    print("hi")
    >>>
        이름이 모나미153, 색이 빨강, 가격이 300
    빠잉
    hi
    빠잉
    ```

