from datetime import datetime, timedelta, timezone

from fastapi.responses import JSONResponse
import jwt


class MenuManager:
    def __init__(self):
        self.jwtkey = "key"
        self.jwtAlgorithm = "HS256"

    def get(self, token):
        try:
            r = jwt.decode(token, self.jwtkey, self.jwtAlgorithm)
            r = {"result":"등록했던 게",
                 "name":r["name"],
                 "price":r["price"]}
        except jwt.ExpiredSignatureError:
            r = {"result": "만료됨요"}
        except jwt.exceptions.DecodeError:
            r = {"result":"토큰 없더요"}
        return r

    def reg(self, name, price):
        r = {
            "result" : "등록 성공",
            "name" : name,
            "price" : price,
            "exp" : datetime.now(timezone.utc) + timedelta(seconds=10)
        }   # 결과는 exp만 빼고 마음대로 (exp는 만료시간)

        jwtr = jwt.encode(r, self.jwtkey, self.jwtAlgorithm)    # 내용, 키, 알고리즘
        # jwtr은 암호화해서 str 한 덩어리로 나옴
        # JSON 형태로 잡아주는 게 좋지 않을까? 
        return JSONResponse({"menuJWT":jwtr})
    
    def update(self, token):
        try:
            r = jwt.decode(token, self.jwtkey, self.jwtAlgorithm)
            r = {"result":"갱신한 게",
                 "name":r["name"],
                 "price":r["price"],
                 "exp" : datetime.now(timezone.utc) + timedelta(seconds=10)
                }
            jwtr = jwt.encode(r, self.jwtkey, self.jwtAlgorithm)    # 내용, 키, 알고리즘
            r = {"menuJWT":jwtr}
        except jwt.ExpiredSignatureError:
            r = {"result": "이미 만료됨요"}
        except jwt.exceptions.DecodeError:
            r = {"result":"토큰 없더요"}
        return r
