## Oracle Python 연동하기
- Python에 통신방식 없으니, 각 DB 메이커에서 만들어준 것 사용
    - cx_oracle.py + instantclient
    - oracledb.py : instantclient가 따로 없어도 되는데  
            구버전 OracleDB는 지원 안돼서, instantclient 따로 필요
            18c는 신버전이라 ㄱㅊ 
- oracledb.py 다운로드(cmd)  
```pip install oracledb```
### Python
```py
