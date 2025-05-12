## MongoDB
NoSQL  
- 테이블 안 나누고 변수 있음 -> subquery/join 없음
- use DB명;

### 접속
- mongosh폴더 가서 cmd
- mongosh 서버 IP주소 
### Create
```db.테이블명.insertOne({멤버변수명:값, 멤버변수명:값, ...});```
- 테이블 따로 안 만들고 그냥 insert하면 됨 
- PK 따로 지정 없이 _id 사용

### Read
기본 조회
- ```db.테이블명.find();```  
- select * from 테이블명;  

조건 조회
- ```db.테이블명.find(JS 객체);```  
- db.테이블명.find(s_price : 3000);
- select * from 테이블명 where s_price = 3000;  

연산자를 포함한 조건 조회
- ```db.테이블명.find({필드명 : {"연산자" : 값});```   
- $gt >, $gte >=, $ne !=. $lte <=, $lt <, $regex like
- db.테이블명.find({s_price : {"$gte" : 3000}});
- select * from 테이블명 where s_price >= 3000;
- db.테이블명.find({s_name : {"$regex" : "포"}});
- select * from 테이블명 where s_name like "포";

and, or가 있는 조건 조회
- ```db.테이블명.find({"$and" : [JS객체, JS객체, ...]});```
    ```
    db.apr14_snack.find({
        "$or" : [
            {s_price : {"$gte" : 3000}},
            {s_name : {"$regex" : "포"}}
        ]
    });```

정렬 조회
- ```db.테이블명.find(JS객체).sort({"필드명" : 1, "필드명" : -1, ...});```
- 1 : 오름차순
- -1 : 내림차순
- ``` db.테이블명.find().sort({s_name : 1});```

예제
- 과자중에 3000 <= 가격 <= 5000인 과자 조회
- 이름 가나다 -> 가격 비싼 순
    ```
    db.apr14_snack.find({
        "$and" : [
        {s_price : {"$gte" : 3000}},
        {s_price : {"$lte" : 5000}}
        ]
    }).sort({s_name:1, s_price:-1});
    ```
### Update
- ```db.테이블명.updateMany(찾을거, {"$set" : 바꿀거});```
    ```
    db.apr14_snack.updateMany(
    {s_name : "포키"},
    {"$set":{s_price:0}}
    );
    ```

### Delete
- ```db.테이블명.deleteMany(찾을거);```
- ```db.apr14_snack.deleteMany({s_name : "포카칩"});```