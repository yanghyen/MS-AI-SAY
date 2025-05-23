## HTTP
### 컴퓨터 통신
- Socket통신(실시간) : 카톡(수신자 의지와 관계없이 발신자가 발신하면 옴)
    - Socket서버 : Node.js(웹소켓서버에 특화)
    - Socket클라이언트 : js/React
- HTTP통신(실시간X) : 인터넷(내가 요청해야 응답 옴)
    - HTTP서버 : Flask
        - 웹페이지 누군가가 요청하면 응답해주자
        - 갖고 있는 데이터 or AI 예측값을 누군가가 요청하면 응답해주자
    - HTTP클라이언트 : js/React
        - 웹 데이터 가져와서 AI훈련용 데이터로 모아두자(Python)
        - AI의 결과 웹페이지에 띄우자(js/React)
- server : 서비스를 제공하는 컴퓨터
- client : 서비스를 이용하는 컴퓨터

|컴퓨터 통신|전화|
|----|----|
|protocol(통신방식)|전화, 영통, 페이스톡,...|
|IP주소(142.250.71.228)|전화번호|
|Domain Name(www.google.com)|번호 저장 후 검색해서 찾음 -> 글자로 저장|
|port(1 ~ 65536) 서비스 구분|???|

### HTTP 통신(http or https)
- 기상청 예시 https://www.weather.go.kr/w/index.do
    - protocol : https(보안 강화)
    - IP주소 : ?
    - 도메인 네임 : www.weather.go.kr
    - 포트 : 443(https 기본)
        - http : 80이 기본
    - w/index.do
        - w : 폴더명
        - index.do : 파일명 
- 세션 : 서버-클라이언트의 연결
    - 유지시간 지나면 자동으로 끊김 
- 요청 방식/HTTP메서드
    - GET, POST
    - ```hc.request("요청방식", "주소 남은 부분")```
- 응답
    ```py
    resBody = res.read()
    print(resBody.decode()) # decode() 보기 편하게 출력됨
    ```
- res, req 약속된 형식 : XML or JSON
    - XML(eXtended Markup Language)
    - 데이터를 HTML 모양으로 표현 
    - DOM 객체
        - <tagName attribute="val"> : startTag
        - text : text
        - </tagName> : endtag
- parsing
    - 받아온 데이터 가공해서 필요한 부분만 추출
- iter VS find()
    - 단수형 vs ㅜㅇㄹ려


### 인터넷 주소 체계
- 프로토콜://서버주소[:포트번호]/폴더/.../파일?param변수명=param값&param변수명=param값&...
- request paprameter
    - 클라이언트가 서버에게 전달해주는 정보
    - 주소로 전달
- request header
    - 클라이언트가 서버에게 전달해주는 정보
    - 내부적으로 전달
    - Python은 dict로 전달
    ```py
    # req header
    h = {
    "X-Naver-Client-Id" : "kTTeIA934puyfjaU8srY",
    "X-Naver-Client-Secret" : "mJCncmRc3F"
    }

    hc = HTTPSConnection("openapi.naver.com")
    hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)
    ```
- 인터넷 주소에는 영어와 숫자만
    - URL 인코딩 필요

### 참고
- library VS framework
    - library : 자주 사용되는 기능 따로 정리해놓고 필요할 때마다 갖다 쓸 수 있게 
    - framework : library + 자체툴