from http.client import HTTPSConnection


hc = HTTPSConnection("www.weather.go.kr") # 폴더, 파일 전까지

hc.request("GET", "/w/index.do")

res = hc.getresponse()  # 응답

# 응답 내용
resBody = res.read()
print(resBody.decode())

hc.close()