import oracledb

# # 구버전 orcleDB
# # init_oracle_client(lib_dir="instantclient폴더경로")

# # 신버전
# init_oracle_client()    # 내장된 instantclient 불러오기

# con = connect("yanghyen/0317@195.168.9.126:1521/xe")    # sqlplus로 접솔할 때 쓰는 형식

# Oracle 데이터베이스에 연결 
con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
print(con)

# 데이터 확보
name = input("상품명 : ")
price = int(input("가격 : "))

# SQL을 str로 (; 빼고)
sql = "INSERT INTO apr03_product VALUES ('%s', %d)" %(name, price)
print(sql)

# DB 관련 작업 다 해주는 매니저
# sql을 DB서버로 전송
# 전송한 sql을 원격실행
# 실행결과 받아와 
# 실행결과
#   CUD : 데이터 몇개 영향 받았는지 결과가 뜸
#   R : 데이터
# cur 자체가 결과
cur = con.cursor()
cur.execute(sql)

if cur.rowcount == 1:
    print("추가 성공")
    con.commit()    # 가 있어야 DB에 반영
# 바로 DB서버에 반영X
# DBeaver는 auto commit
# 체크해보고 맞다 : commit
# 체크해봤는데 아닌 게 존재 : rollback

cur.close()
con.close()

