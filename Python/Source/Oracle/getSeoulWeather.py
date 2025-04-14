from datetime import datetime
from json import loads
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
import oracledb

APIKEY = "baff8f3c6cbc28a4024e336599de28c4"

hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?&lat=34.9875205&lon=135.7592518&&appid=" + APIKEY + "&units=metric&lang=kr")
con = oracledb.connect(user="yanghyen", password="0317", dsn="195.168.9.126:1521/xe")
cur = con.cursor()

resBody = hc.getresponse().read()
weatherData = loads(resBody)

hc.close()
# ---------------------------------------
desc = weatherData["weather"][0]["description"]
temp = weatherData["main"]["temp"]
feelsLike = weatherData["main"]["feels_like"]
humi = weatherData["main"]["humidity"]
data = "'%s','%.2f','%.2f','%d'" % (desc, temp, feelsLike, humi)
sql = 'INSERT INTO seoul_weather VALUES (' + data + ')'
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