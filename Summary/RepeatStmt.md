## 반복문
### while
- 조건 따져서 반복
- while VS do while
    - while : 조건 보고 실행, 한번도 실행 안 할수도
    - do while : 실행 후 조건 검사, Python에 없음
```py
while (계속 진행할 조건):
```

### for
- for 변수 in 컬렉션:  
    내용
- dictionary에 추천되는 사용법
    - .items() : 
    ```py
    c = {"기온" : 20, "미세먼지" : "심함"}
    for v in c.items():
        print(v, type(v))
    >>>
    ('기온', 20) <class 'tuple'>
    ('미세먼지', '심함') <class 'tuple'>
    ```
    
### 반복문 제어
- break : 반복문 종료
- continue : 턴 종료 
    ```py
    for i in range(10):
        if i == 3:
            continue    # 남은 8번줄 안 하고 바로 올라감
        print(i)
    ```
- 무한 루프 : while True
    - while 문법 구조상 조건식 먼저 써야 되는데 애매할 때 사용
- 참고
    - JAVA에는 각 반복문에 a, b, c처럼 네이밍 가능해서 ```break a``` 하면 반복문 a만 종료됨 
    ```java
    public static void main(String[] args) {
        a : for (int i = 0; i < 5; i++) {
            b : for (int j = 0; j < 5; j++) {
                if (j == 3) {
                    break a;
                }
                System.out.printl(i, j)
            }
        }
    }
    ```
    - == True 는 생략 가능
    - == False 는 not 어쩌고