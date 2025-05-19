# 평균가

import oracledb

con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
sql = "select avg(p_price) from apr03_product"

cur = con.cursor()

# 실행
cur.execute(sql)

# 결과 처리
# for p in cur:
#     print(p)  # p의 타입은 tuple

for p in cur:
    print(p[0])


    
cur.close()
con.close()