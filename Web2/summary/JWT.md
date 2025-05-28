# JWT
### 목적
- 데이터를 BE에 저장 : 공용 데이터
- 사용자마다 개별 데이터가 필요함  
### 기존 기술
- session : 서버 - 사용자의 연결에 저장 -> 연결 끊으면 데이터 삭제
    - session 유지시간(조절가능)동안 가만히 있으면 연결 끊김
    - 서버가 바뀌면 관리 어려움
    - 근데 요청 날리면 유지시간이 자동갱신됨
- cookie : 사용자PC에 파일로 저장 
    - 연결 끊든 말든, 재부팅하든 말든 유지시간동안 데이터 남음 
    - 보안상 위험
## JWT(Json Web Token)
- JSON + 암호화 + 시간제한
- ```pip install pyjwt```
- exp에 넣을 값 : datetime 이용
    - 현재시간날짜 : datetime.today()
    - 현재시간날짜 : datetime.now()
    - 현재시간날짜(표준 시간대) : datetime.now(timezone.utc)
    - 현재시간날짜(표준 시간대)로부터 10초 지나서 : datetime.now(timezone.utc) + timedelta(seconds=10)
    - 자동갱신X, 수동갱신X -> 똑같은 내용으로 다시 만들기
### 등록  
```py
# BE
def reg(self, name, price):
    r = {
        "result" : "등록 성공",
        "name" : name,
        "price" : price,
        "exp" : datetime.now(timezone.utc) + timedelta(seconds=10)
    }   # 결과는 exp만 빼고 마음대로 (exp는 만료시간)
    jwtr = jwt.encode(r, "key", "HS256")    # 내용, 키, 알고리즘
    return JSONResponse({"menuJWT":jwtr})   # jwtr을 JSON형태로 잡아주기
```
```js
const getResult = () => { 
    axios
    .get(`http://195.168.9.206:1717/menu.reg?name=${menu.name}&price=${menu.price}`)
    .then((res) => { 
        // sessionStorage : 브라우저 닫을 때까지 쓸 수 있는 공간
        // -> 다른 페이지에서도 사용 가능
        sessionStorage.setItem("myJWT", res.data.menuJWT);
        alert(JSON.stringify(res.data.menuJWT));
        setMenu({})
    })
};
```

- jwtr은 암호화해서 str 한 덩어리로 나옴
- jwtr을 JSON형태로 잡아주기
### 복호화(암호 풀기)
