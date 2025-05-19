from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

from pymongo import MongoClient

from yang.stringCleaner import stringCleaner


q = "진격거" 
q = quote(q)

# req header
h = {
   "X-Naver-Client-Id" : "kTTeIA934puyfjaU8srY",
   "X-Naver-Client-Secret" : "mJCncmRc3F"
}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)

resBody = hc.getresponse().read()
hc.close()

# 연결
con = MongoClient("195.168.9.126")
db = con.hyen

for n in fromstring(resBody).iter("item"):
    news = {"title" : stringCleaner.clean(n.find("title").text),
            "desc" : stringCleaner.clean(n.find("description").text)}
    result = db.apr14_naverNews.insert_one(news)
if result.acknowledged:
    print("추가 성공!")

con.close()
