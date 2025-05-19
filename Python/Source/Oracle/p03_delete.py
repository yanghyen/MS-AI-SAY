import oracledb


con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")

# 입력한 단어가 포함된 단어 삭제
name = input("단어 : ")
name = "%" + name + "%"
# sql = "DELETE FROM APR03_PRODUCT"
# sql += " WHERE P_NAME LIKE ''%'||%s||'%''" % name
sql = "DELETE FROM apr03_product"
sql += " WHERE P_NAME LIKE '%s'" % name
print(sql)

cur = con.cursor()
cur.execute(sql)
print(con)
if cur.rowcount == 1:
    print("삭제 성공!")
    con.commit()

cur.close()
con.close()