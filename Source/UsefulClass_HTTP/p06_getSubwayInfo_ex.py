from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("C://Yang/subway.csv", "a", encoding="utf-8")

for dd in range(1, 35):
    try:
        when = "201511%02d" %dd
        hc.request(
            "GET", 
            "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/" + when
        )
        resBody = hc.getresponse().read()

        for s in fromstring(resBody).iter("row"):
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
    except:
        print("유효하지 않은 날짜입니다.")
f.close()
hc.close()