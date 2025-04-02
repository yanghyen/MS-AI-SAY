from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring


hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")

resBody = hc.getresponse().read()
print(resBody.decode())
hc.close()
######################################
# 오늘 데이터까지만 출력
# kmaWeather.csv에
f = open("C:/Yang/kmaWeather.csv", "a", encoding="utf-8")
weatherData =  fromstring(resBody)
weathers = weatherData.iter("data")
for w in weathers:
    if (w.find("hour").text == "3"): 
        break
    f.write(w.find("hour").text + ",")
    f.write(w.find("temp").text + ",")
    f.write(w.find("wfKor").text + "\n")

f.close()

# 매일 아침마다 
# .bat 만들어서 바탕화면에 놓고 클릭
# -> 윈도우 스케쥴러로 자동 실행 (찾아보기)
# 는 아니고
# Linux 서버에 올려서 + 리눅스 스케쥴러