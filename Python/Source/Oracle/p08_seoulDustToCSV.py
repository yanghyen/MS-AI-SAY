# DB(seoul_dust)내 데이터 .csv로 변환하기
from datetime import datetime
import oracledb

con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
f = open("C:/Yang/seoulDustAnalysis.csv", "a", encoding="utf-8")

sql = "select * from seoul_dust"
cur = con.cursor()
cur.execute(sql)

# 내가 한 거
# for p in cur:
#     dateData = p[0]
#     dateData = datetime.strftime(dateData, "%Y,%m,%d")
#     area = p[1]
#     district = p[2]
#     pm10 = p[3]
#     pm25 = p[4]
#     category = p[5]
#     data = "%s,%s,%s,%s,%s,%s\n" %(dateData, area, district, pm10, pm25, category)
#     f.write(data)

# 쓰앵님이 하신 거
for date, area, district, pm10, pm25, category in cur:
    date = datetime.strftime(date, "%Y,%m,%d")
    f.write("%s,%s,%s,%d,%d,%s\n" % (date, area, district, pm10, pm25, category))
print("저장완료!")
f.close()
cur.close()
con.close()