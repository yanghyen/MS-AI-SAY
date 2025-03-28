# 2015 ~ 2024
# bus.csv
# 2015,01,01,100번(하계동~용산구청),명륜3가.성대입구,108,171

from http.client import HTTPConnection
from json import loads

hc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("C://Yang/bus.csv", "a", encoding="utf-8")
for yy in range(15, 25):
    for mm in range(1, 13):
        for dd in range(1, 32):
            try:
                when = "20%02d%02d%02d" % (yy, mm, dd)
                hc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/1000/+" + when + "/")
                resBody = hc.getresponse().read()
                busData = loads(resBody)
                rowData = busData['CardBusStatisticsServiceNew']['row']
                if rowData != None:
                    for b in rowData:
                        busDate = b["USE_YMD"]
                        y = busDate[0:4]
                        m = busDate[4:6]
                        d = busDate[6:8]
                        busNum = b["RTE_NM"]
                        stationName = b["SBWY_STNS_NM"]
                        getOn = b["GTON_TNOPE"]
                        getOff = b["GTOFF_TNOPE"]
                        totalData = "%s,%s,%s,%s,%s,%d,%d\n" %(y, m, d, busNum, stationName, getOn, getOff)
                        f.write(totalData)
                print(when)
            except:
                print("메롱")



f.close()


hc.close()