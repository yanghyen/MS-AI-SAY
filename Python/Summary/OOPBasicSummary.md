## OOD(Design)
- OOP : real world 묘사
- 객체지향스럽게 설계
1. 실제로 비만도 검사센터 가서 검사받는 상황 생각
2. 등장인물(프로그램에 필요한 것만 남겨) : 의사, 환자
3. 속성(프로그램에 필요한 것만 남겨) : 이름, 나이, ...
4. 상황 진행 -> 액션
5. ㄱㄱ(최대한 실생활스럽게)

### 객체 간의 관계
- has a : 속성
- is a : 상속
    - "Taxi is a Car" 성립
    - OOP가 말하는 상속 사용 가능
- 다른 PL : 기본형, 객체 존재
- Python : 객체만 존재

### 상속
- Pen is a Product
    - Product : 상위클래스, 부모클래스
    - Pen : 하위클래스, 자식클래스
    ```py
    class Product:
        pass
    class Pen(Product):
        pass
    ```
- Product에 있는 멤버들(멤버변수, 메소드)이 Pen에도 전달됨
- 다른 PL : 생성자는 상속X
- Python : 생성자 상속O <= 생성자에서 멤버변수를 정해서
- overriding : 상속받은 메소드 기능 바꾸기
    - 상속은 주로 기능 추가!
    - self : 자신
    - super : 상위클래스
    ```py
    def showInfo(self):
        super().showInfo() # Product의 showInfo 호출 -> 이름, 가격
        print(self.color)
    ```
    - 다단상속 : 상속받은 걸 상속받기
- 다중상속 : 여러 클래스로부터 상속받음
    - 대부분 PL : 안됨 <= 멤버 이름 같으면 애매함
    - Python : 가능티비 
        - 멤버 이름 같으면 먼저 쓴 거

### 찾아보기
- call by value:
- call by reference