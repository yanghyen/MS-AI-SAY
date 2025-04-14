from pymongo import MongoClient
# pymongo : MongoDB 명령어 거의 그대로 사용하게 해줌


con = MongoClient("195.168.9.126")
print(con)
db = con.hyen # con.DB명
print(db)
con.close()