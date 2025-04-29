# ClientID : kTTeIA934puyfjaU8srY
# ClientSecret : mJCncmRc3F

from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

from hyenLib.stringCleaner import stringCleaner


q = "산불" 
q = quote(q)

# req header
h = {
   "X-Naver-Client-Id" : "kTTeIA934puyfjaU8srY",
   "X-Naver-Client-Secret" : "mJCncmRc3F"
}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)

resBody = hc.getresponse().read()
# print(resBody.decode())
hc.close()

for n in fromstring(resBody).iter("item"):
    print(stringCleaner.clean(n.find("title").text))
    print(stringCleaner.clean(n.find("description").text))
    print("------------")
