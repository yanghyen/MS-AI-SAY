from http.client import HTTPSConnection
from urllib.parse import quote


class NaverNewsDAO:
    def getNews(self, searchTxt):
        q = quote(searchTxt)
        h = {
        "X-Naver-Client-Id" : "kTTeIA934puyfjaU8srY",
        "X-Naver-Client-Secret" : "mJCncmRc3F"
        }

        hc = HTTPSConnection("openapi.naver.com")
        hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)

        resBody = hc.getresponse().read()
        hc.close()

        return resBody
