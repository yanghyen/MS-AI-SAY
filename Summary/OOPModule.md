# package
- 

## import
- 안 해도 되는데, 하면 문법이 간단해짐
- Python은 다른 모듈에 있는 거 불러오려면 무조건 해야 됨
1. import 패키지명.모듈명
2. import 패키지명.모듈명 as 별칭
    ```py
    import animal.pet as ap
    c = ap.Cat("나밍", 13)
    c.showInfo()
    ```
3. from 패키지명.모듈명 import 가져올 거
    ```py
    from animal.pet import Cat
    c = Cat("나밍", 140)   # 바로 쓸 수 있음
    ```
- Window에 PYTHONPATH 설정하면 프로젝트도 인식 가능
    - Linux에서 실행할거라 굳이 안 해도 됨
- import한 class와 해당 파일에서 생성한 class 이름 중복되면? / A에서 받은 class와 B에서 받은 class 이름 중복되면?
    - 패키지명/모듈명이 아예 생략되는 3번이 무조건 좋은 게 아니란 뜻
    - 1, 2번 스타일도 필요
- 서로 import하면 ```most likely due to a circular import``` 에러 뜸
    - Python은 import가 꼭 맨 위에 있지 않아도 돼서 이런 식으로 해결
    ```py
    if __name__ == "__main__":
        from p02_oopModule import BoardMarker
        bm = BoardMarker("merong", 13)
        bm.showww()
    ```
