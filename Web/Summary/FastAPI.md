## FastAPI
- flask : 자체 WAS 기능 포함 -> 단독실행
- fastapi : 자체 WAS 기능이 없어서 따로 필요함
    - 기본적으로 json 응답
    - ```pip install uvicorn[standard]```
    - 터미널에서 밑에 명령어로 실행  
    ```uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload```

### Web
1. 클래식 웹
- back-end(FastAPI)
    - 프로그램스러운 작업 다 해서
    - HTML + CSS +JS 완성시켜서 응답
- front-end(JavaScript)
    - 완성된 웹사이트에 효과 부여
2. 신형 웹
- back-end(FastAPI)
    - DB 관련 작업만
    - 결과를 FE에서 쓸 수 있게(XML/JSON 응답)
- front-end(JavaScript)
    - 프로그램스러운 작업 다 하자
    - DB관련 작업은 BE쪽 통해서 (AJAX(XML/JSON 파싱))