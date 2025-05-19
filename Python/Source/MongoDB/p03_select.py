from pymongo import ASCENDING, DESCENDING, MongoClient


# 연결
con = MongoClient("195.168.9.126")
db = con.hyen

# snacks = db.apr14_snack.find()
snacks = db.apr14_snack.find().sort([("s_price", DESCENDING), ("s_name", ASCENDING)])

for s in snacks:
    print(s["s_name"])
    print(s["s_price"])
    print('---------')

con.close()