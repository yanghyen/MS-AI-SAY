from datetime import datetime
import oracledb

con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
f = open("C:/Yang/seoulWeatherAnalysis.csv", "a", encoding="utf-8")

sql = "select * from seoul_weather"
cur = con.cursor()
cur.execute(sql)

for desc, temp, feelsLike, humi in cur:
    f.write("%s,%.2f,%.2f,%d \n" % (desc, temp, feelsLike, humi))
print("저장완료!")
f.close()
cur.close()
con.close()