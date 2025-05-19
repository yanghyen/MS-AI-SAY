# 서울시 미세먼지 데이터를 저장하는 프로그램
# seoulDust.csv
# 2025,03,26,17,도심권,중구,70,17,보통

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

resBody = hc.getresponse().read()
# print(resBody.decode())
hc.close()
# ---------------------------------------
f = open("C:/Yang/seoulDust.csv", "a", encoding="utf-8")
dustData = fromstring(resBody)
dusts = dustData.iter("row")

def getDustInfo():
    for d in dusts:
        try:
            writeDustData(d)
        except Exception as e:
            f.write("\n")
            print(f"Error: {e}")

def parseDate(msrdt):
    return ",".join([msrdt[0:4], msrdt[4:6], msrdt[6:8], msrdt[8:10]])

def writeDustData(d):
    data = [
        parseDate(d.find("MSRDT").text),
        d.find("MSRRGN_NM").text,  
        d.find("MSRSTE_NM").text,  
        d.find("PM10").text,  
        d.find("PM25").text,  
        d.find("IDEX_NM").text  
    ]
    f.write(",".join(str(item) for item in data) + "\n")

getDustInfo()
f.close()