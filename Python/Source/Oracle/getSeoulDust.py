# 실시간 미세먼지 데이터 내 DB에 저장하기
from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import oracledb


hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/100/")
con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
cur = con.cursor()

resBody = hc.getresponse().read()
hc.close()
# ---------------------------------------
for r in fromstring(resBody).iter("row"):
    msrrgn_nm = r.find("MSRRGN_NM").text
    msrste_nm = r.find("MSRSTE_NM").text
    pm10 = r.find("PM10").text
    pm25 = r.find("PM25").text
    idex_nm = r.find("IDEX_NM").text
    data = "sysdate,'%s','%s',%s,%s,'%s'" %(msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)
    sql = 'INSERT INTO seoul_dust VALUES (' + data + ')'
    print(sql)  
    try :
        cur.execute(sql)
        if cur.rowcount != None:
            print("추가 성공")
            con.commit()
    except Exception as e:
        print(e)



cur.close()
con.close()