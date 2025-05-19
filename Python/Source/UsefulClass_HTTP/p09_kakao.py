# dev.kakao.com
# 로그인

REST_API_KEY = "e92cda242e0b9a62ccb0f66df2081e0a"

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

h = {
    "Authorization": f"KakaoAK {REST_API_KEY}"
}
what = quote(input("뭐 먹을랭 : "))

hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", "/v2/local/search/keyword.json?y=37.5381529&x=127.0673498&query=" + what, headers=h)
resBody = hc.getresponse().read()
hc.close()
data = loads(resBody)
# for i in range(len(data["documents"])):
#     print(data["documents"][i]["place_name"])
#     print(data["documents"][i]["road_address_name"])
#     print(data["documents"][i]["distance"])
#     print(data["documents"][i]["phone"])
for l in data["documents"]:
    print(l["place_name"])