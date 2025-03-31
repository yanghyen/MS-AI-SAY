from http.client import HTTPConnection
from json import loads

yy = 2017
hc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("C://Yang/bus%d.csv" % yy, "a", encoding="utf-8")

# for yy in range(2015, 2025):
for mm in range(1, 13):
    for dd in range(1, 32):
        for start in range(1, 41002, 1000):
            t = "%d/%d/%d%02d%02d" %(start, start+999, yy, mm, dd)
            hc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/" + t)
            resBody = hc.getresponse().read()

            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData:
                cbssn = busData['CardBusStatisticsServiceNew']
                for b in cbssn["row"]:
                    busDate = b["USE_YMD"]
                    y = busDate[0:4]
                    m = busDate[4:6]
                    d = busDate[6:8]
                    busNum = b["RTE_NM"].replace(",",".")
                    stationName = b["SBWY_STNS_NM"].replace(",",".")
                    getOn = b["GTON_TNOPE"]
                    getOff = b["GTOFF_TNOPE"]
                    totalData = "%s,%s,%s,%s,%s,%d,%d\n" %(y, m, d, busNum, stationName, getOn, getOff)
                    f.write(totalData)
        print(yy, mm, dd)




hc.close()
f.close()
