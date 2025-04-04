import oracledb


con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")

name = input("찾을 상품명 : ")
price = int(input("변경할 가격 : "))

sql = "update apr03_product set p_price = %d" % price
sql += " where p_name = '%s'" % name

cur = con.cursor()
cur.execute(sql)

if cur.rowcount == 1:
    print("수정 성공")
    con.commit()

cur.close()
con.close()