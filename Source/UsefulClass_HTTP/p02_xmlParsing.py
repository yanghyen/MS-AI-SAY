from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring


hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")

resBody = hc.getresponse().read()
print(resBody.decode())
hc.close()

weatherData =  fromstring(resBody)
weathers = weatherData.iter("data")
print(weathers)
for w in weathers:
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    print("----------")