from pymongo import MongoClient


# 연결
con = MongoClient("195.168.9.126")
db = con.hyen

# 데이터 확보
name = input("이름 : ")
price = int(input("가격 : "))

# 명령어 서버로 전송 + 원격실행 + 결과받기 
result = db.apr14_snack.insert_one({"s_name":name, "s_price":price})

if result.acknowledged:
    print("추가 성공!")

con.close()
