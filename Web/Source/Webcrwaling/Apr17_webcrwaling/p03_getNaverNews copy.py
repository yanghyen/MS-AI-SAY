# https://news.naver.com/ 에서 데이터 파싱해오기

from http.client import HTTPSConnection

from bs4 import BeautifulSoup


con=HTTPSConnection("news.naver.com")
con.request("GET","/")
rb=con.getresponse()
pp=rb.read()
con.close()

# beautifulsoup 
# 웹사이트에서 받아온 거, 내장 html파서 이름, 그 사이트 인코딩 방법
cafeData=BeautifulSoup(pp,"html.parser",from_encoding="utf-8")
snsTxts=cafeData.select(".a")
for s in snsTxts:
    print(s.text)