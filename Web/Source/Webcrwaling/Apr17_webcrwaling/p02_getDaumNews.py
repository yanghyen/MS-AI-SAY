# https://news.daum.net/ 사이트에서 파싱하기 
# 페이지에 있는 뉴스 제목들을 불러와봐라

from http.client import HTTPSConnection

from bs4 import BeautifulSoup


con=HTTPSConnection("news.daum.net")
con.request("GET","/")
rb=con.getresponse().read()
con.close()

# beautifulsoup 
# 웹사이트에서 받아온 거, 내장 html파서 이름, 그 사이트 인코딩 방법
newsData=BeautifulSoup(rb,"html.parser",from_encoding="utf-8")
for s in newsData.select(".list_newsheadline2 .tit_txt"):
    print(s.text)