### 제어 코드
- \n : new line (줄만 바꾸기)
    ```py
    print("aa\nbb")
    >>>
    aa
        bb
    ```
- \r : carriage return (커서를 맨 앞으로)
    ```py
    print("aa\rbb")
    >>>
    bb
    ```
- 제대로 된 엔터 : \r\n
    ```py
    print("aa\r\nbb")
    >>>
    aa
    bb
    ```
- \t : tab (글자수가 아닌 tab point로 이동)
- \b : backspace (1byte 지우기)
    - C : 1글자 당 1byte
    - Python, Java : 1글자 당 2byte  
    => \b 성립X
- \\\ : \ 출력
    ```
    # 경로 쓸 때
    print("C:\\notion\Python\workspace")
    ```
    - Python은 고급언어라서 제어 코드 아니면 자동적으로 \로 처리
- \\" : " 출력  

### 출력
- %d : 정수 데이터 들어갈 자리
    - %05d : 0 채워서 5자리 출력
    ```py
    age = 10
    print("나이 : %d살" % age)
    print("나이 : %05d살" % age)

    >>>
    나이 : 10살
    나이 : 00010살
    ```
- %f : 실수 데이터 들어갈 자리
    - %.3f : 소수점 이하 3자리(반올림)
- %s : 글자 데이터 들어갈 자리
- %d : 논리형 데이터 들어갈 자리
- %% : % 출력

### 참고
- abcd : Python 문법
- "abcd" : 글자 데이터
- "" : 여러 글자
- '' : 한 글자  
- encoding : utf-8 주력
    ```py
    # 이건 주석이 아님
    # -*- coding:utf-8 -*-
    print("ㅎㅅㅎ")
    print("ㅎㅅㅎ")
    print("ㅎㅅㅎ")

    print("ㅎ", end='')
    print("ㅅㅎ")

    >>>
    ㅎㅅㅎ
    ㅎㅅㅎ
    ㅎㅅㅎ
    ㅎㅅㅎ
    ```
- 콘솔출력 : 중간 테스트