### 함수 vs 메소드
- 변수(variable) : 데이터 담는 그릇 => 명사형
- 함수(function) : 액션들 모아놓은 그릇 => 동사형
- 메소드(method) :

### 메인 함수 영역
- 다른 PL : main 함수 영역이 따로 있음
    - main 영역 내에 함수 정의X
    - 띄어쓰기, 엔터 무의미
    <= 영역을 {}로 표시
    - parameter(개수, 자료형) 다르면 함수명 같아도 됨
- Python : interpreter방식 언어라 따로 없음
    - interpreter방식 : 소스 한 줄씩 직접 해석 후 실행
    - 띄어쓰기, 엔터 유의미
    <= 영역을 :과 들여쓰기로 표시
    1. 정의 
    - 함수명 규칙 == 변수명 규칙 
    - parameter : 함수 수행시 필요한 재료
    - return 값 : 값을 되돌려주고 함수 끝
        - Python에서 여러 값 return되는 것처럼 보여도 tuple로 받아지는 거임
        => collection으로 받자
        - 안 받아도 되는 값은 변수명 ㄴㄴ => _로 받기
    2. 함수 호출
    ```py
    def test():
        pass    # 자리 채우기
    ```
    - overloading 불가
    - lambda 함수 : 무명의 1회용 함수
        ```py
        (lambda x:print("양혜인" * x))(3)
        ```
        - 값 간단하게 구할 때
        ```py
        # a + b return하고 싶을 때
        c = (lambda a, b:a+b)(1, 2)
### recursive(재귀적) 호출
- 함수 내부에서 자기자신을 호출해서 반복이 생기게 함
- recursive 제한 횟수 설정
    - 계산용은 아님 
- 예시) 숫자 넣으면 그 숫자까지 합을 구해주는 함수
```py
def getSum(x):
    if x == 1:
        return 1
    return getSum(x-1) + x

a = getSum(19)
```
- 함수는 가독성이 좋아 사람에게 좋지만, 컴퓨터에서는 JUMP 연산을 쓰기 때문에 시간이 오래 걸린다

### 참고
- 작명 팁
    - 동사 앞으로 정렬 -> 기능별 정렬
    - 동사 뒤로 정렬 -> 주제별 정렬
        printSum VS sumPrint
- overriding VS overloading
    - overriding : 부모 클래스의 메소드를 **자식 클래스**에서 재정의하는 것
    - overloading : 같은 이름의 메소드를 여러 개 정의하는 것.      
        - JAVA
            - 파라미터 다르면 함수명 같아도 됨 => 일부러 같게 
            - 생성자 다양하게 만들어두고, 필요한 것들 갖다 씀
        - Python
            - 구조상 overloading 불가능 = 생성자 하나만 가능
            - 생성자 여러개 만들어놓고 필요한 거 갖다쓰기 불가능
- Call By Value, Call By Reference
    - Call By Value : 함수 호출 시 값 넣어서 호출
    - Call By Reference : 함수 호출 시 주소값 넣어서 호출 (Python)