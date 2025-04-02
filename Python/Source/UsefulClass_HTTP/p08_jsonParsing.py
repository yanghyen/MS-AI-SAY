# API key : baff8f3c6cbc28a4024e336599de28c4
# https://
# api.openweathermap.org
# /data/2.5/weather
# ?
# q=seoul
# &
# appid=baff8f3c6cbc28a4024e336599de28c4
# (option)
# &
# units=metric  섭씨온도
# &
# lang=kr   한국어

# 교토타워 !3d34.9875205!4d135.7592518!


from http.client import HTTPSConnection
from json import loads
APIKEY = "baff8f3c6cbc28a4024e336599de28c4"
where = "seoul"

hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?&lat=34.9875205&lon=135.7592518&&appid=" + APIKEY)
resBody = hc.getresponse().read()
print(resBody.decode())
# ------------------
weatherData = loads(resBody)

desc = weatherData["weather"][0]["description"]
temp = weatherData["main"]["temp"]
humi = weatherData["main"]["humidity"]
print(desc)
print(temp)
print(humi)