# 객체지향적으로 정리해보기
# 2015/01/01 ~ 2024/12/31 전체 지하철 운행정보
# subway.csv로
# 날짜, 노선, 역, 탄 승객 수, 내린 승객 수
# 2015,01,01,1호선,서울역,14323,23433
from datetime import datetime, timedelta
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


def getDate():
    startDay = "20150101"
    startDay = datetime.strftime(startDay, "%Y%m%d")
    endDay = "20150101"
    endDay = datetime.strftime(endDay, "%Y%m%d")
    currentDay = startDay + timedelta(days = 1)
    i = 0
    while (currentDay < endDay):
        try:
            currentDay = startDay + timedelta(days = 1)
            
        except:
            pass


def getData(date):
    hc = HTTPConnection("openapi.seoul.go.kr:8088")
    hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/10/20151101/")
    resBody = hc.getresponse().read()
    for s in fromstring(resBody).iter("row"):
        useYmd = s.find("USE_YMD").text
        lineName = s.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
        stationName = s.find("SBWY_STNS_NM").text.replace(",", ".")
        getOn = s.find("GTON_TNOPE").text
        getOff = s.find("GTOFF_TNOPE").text
        data = "%s,%s,%s,%s,%s\n" %(useYmd, lineName, stationName, getOn, getOff)
        print(data)

getData()