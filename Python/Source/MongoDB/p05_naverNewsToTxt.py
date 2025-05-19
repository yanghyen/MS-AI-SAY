from xml.etree.ElementTree import fromstring
from pymongo import MongoClient
from yang.stringCleaner import stringCleaner


con = MongoClient("195.168.9.126")
db = con.hyen

f = open("C:/Yang/docs/mongoNaverNews/naverNews.txt", "a", encoding="utf-8")
for n in db.apr14_naverNews.find():
    f.write(n["title"] + "\t")
    f.write(n["desc"] + "\n")

con.close()
f.close()