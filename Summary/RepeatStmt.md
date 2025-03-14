## 반복문
### while
- 조건 따져서 반복

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
    
