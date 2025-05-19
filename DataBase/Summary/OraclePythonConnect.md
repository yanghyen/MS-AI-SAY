## Oracle Python 연동하기
- Python에 통신방식 없으니, 각 DB 메이커에서 만들어준 것 사용
    - cx_oracle.py + instantclient
    - oracledb.py : instantclient가 따로 없어도 되는데  
            구버전 OracleDB는 지원 안돼서, instantclient 따로 필요
            18c는 신버전이라 ㄱㅊ 
- oracledb.py 다운로드(cmd)  
```pip install oracledb```
- cursor : DB 관련 작업 다 해주는 매니저
    - sql을 DB서버로 전송
    - 전송한 sql을 원격실행
    - 실행결과 자체이기도 함 
        - CUD : 데이터 몇개 영향 받았는지 결과가 뜸
        - R : 데이터
### SELECT 
```py
import oracledb

# python과 orcleDB 연동
con = oracledb.connect(user="DBID", password="DBPW", dsn="DBIP:port/SID")

# sql문 작성
sql = "select * from apr03_product"

cur = con.cursor()

# 실행
cur.execute(sql)

# 결과 처리
# for p in cur:
#     print(p)  # p의 타입은 tuple

for n, p in cur:
    print(n)
    print(p)
    print('---------')

cur.close()
con.close()
```
### CUD
- con.commit()이 있어야 변경사항이 DB에 실제로 반영됨
    - 체크해보고 맞다 : commit
    - 체크해봤는데 아닌 게 존재 : rollback
    - DBeaver는 auto commit이라 commit 불필요
- update 예시
```py
import oracledb

con = oracledb.connect(user="DBID", password="DBPW", dsn="DBIP:port/SID")

name = input("찾을 상품명 : ")
price = int(input("변경할 가격 : "))

# sql문을 여러 줄로 써야 할 때
# where 앞에 띄어쓰기 주의!
sql = "update apr03_product set p_price = %d" % price
sql += " where p_name = '%s'" % name

cur = con.cursor()
cur.execute(sql)

# rowcount : 변화된 줄 수
if cur.rowcount == 1:
    print("수정 성공")
    con.commit()

cur.close()
con.close()
```