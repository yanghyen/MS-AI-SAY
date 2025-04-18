## FastAPI
- flask : 자체 WAS 기능 포함 -> 단독실행
- fastapi : 자체 WAS 기능이 없어서 따로 필요함
    - 기본적으로 json 응답
    - ```pip install uvicorn[standard]```
    - 터미널에서 밑에 명령어로 실행  
    ```uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload```
