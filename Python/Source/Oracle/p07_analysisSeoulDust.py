# 권역별 미세+초미세 평균 
# 안 좋은 순서대로 정렬
import oracledb

con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")

sql = "select s_area, avg(s_pm10 + s_pm25) from seoul_dust"
sql += " group by s_area order by avg(s_pm10 + s_pm25) desc"
cur = con.cursor()
cur.execute(sql)

for mn, avg in cur:
    print(mn, avg)

cur.close()
con.close()