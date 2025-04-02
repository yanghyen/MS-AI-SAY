from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

resBody = hc.getresponse().read()
# print(resBody.decode())
hc.close()
# ---------------------------------------
now = datetime.today()
now = datetime.strftime(now, "%Y,%m,%d,%H")
f = open("C:/Yang/seoulDustEx.csv", "a", encoding="utf-8")
for r in fromstring(resBody).iter("row"):
    msrrgn_nm = r.find("MSRRGN_NM").text
    msrste_nm = r.find("MSRSTE_NM").text
    pm10 = r.find("PM10").text
    pm25 = r.find("PM25").text
    idex_nm = r.find("IDEX_NM").text
    data = "%s,%s,%s,%s,%s,%s\n" %(now, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)
    f.write(data)
f.close()