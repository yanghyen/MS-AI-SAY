from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("C://Yang/subway3.csv", "a", encoding="utf-8")

for yy in range(15, 16):
    for mm in range(1, 3):
        for dd in range(1, 10):
            when = "20%d%02d%02d" %(yy, mm, dd)
            hc.request(
                "GET", 
                "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/" + when
            )
            resBody = hc.getresponse().read()

            stations = fromstring(resBody).iter("row")
            if stations != None:
                for s in stations:
                    # print(s.find("USE_YMD").text)
                    use_ymd = s.find("USE_YMD").text
                    y = use_ymd[0:4]
                    m = use_ymd[4:6]
                    d = use_ymd[6:8]
                    lineName = s.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
                    stationName = s.find("SBWY_STNS_NM").text.replace(",", ".")
                    getOn = s.find("GTON_TNOPE").text
                    getOff = s.find("GTOFF_TNOPE").text
                    data = "%s,%s,%s,%s,%s,%s,%s\n" %(y, m, d, lineName, stationName, getOn, getOff)
                    f.write(data)
                print(when)
f.close()
hc.close()