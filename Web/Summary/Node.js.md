# Node.js
- 실시간 통신 !!!
- 채팅, 게임, ReverseAJAX
1. singlethread : 기본적으로 컴퓨터는 한번에 한 작업만 가능
2. multithread : Python이 약함, 컴퓨터 부담 증가

- 지금까지 한 FastAPI는 singelthread

- single thread blocking I/O 
    - 10분
    - FastAPI 기본
- multi thread blocking I/O 
    - 5분 동생들 보내
    - JSP/Spring/SpringBoot
- single thread non-blocking I/O 
    - 5분 중간에서 기다려
    - FastAPI(async + await), Node.js

### FastAPI VS Node.js
1. FastAPI
- Python
- uvicorn WAS에 실어서
- Python 라이브러리

2. Node.js
- JavaScript
- 단독 실행
- JS 독립 프레임워크
- npm(node package manager) 활용해서 다양한 add-on
    - npm install 이름 -g : Node.js 본체에 붙이는 툴
    - npm install 이름 : 프로젝트에 넣는 라이브러리
### Node.js 시작하기
1. Node.js 본체 설치
2. nodemon 설치
    - 시작 - cmd - npm install nodemon -g
3. express : 웹 백엔드 프로젝트 자동생성
    - npm install express -g
    - npm install express-generator@4 -g
### 프로젝트 생성
1. 프로젝트 만들 곳 가서 cmd
2. ```express 프로젝트명```
3. 프로젝트 폴더로 들어가서 ```cd 프로젝트명```
4. 기본적으로 필요한 라이브러리 설치
    - ```npm install```
5. 실행(nodemon)
- ```nodemon app.js```
6. VScode에서 app.js 편집
### 참고
- app.js
    - ```app.listen(5643); // Node.js Express WAS 포트 번호```
- mongojs(Node.js + MongoDB 연동 라이브러리 설치)
    - Node.js : JS로 BE 프로그래밍
    - MongoDB : JS로 제어
    - mongojs : MongoDB 명령어 그대로 쓰게 + 콜백함수
    - npm install mongojs
    - ```js
        var db = mjs("195.168.9.126/yanghyenTS", ["may12_snack"]);
        var n = rq.query.name;
- 웹소켓서버 구현에 최적화
    1. js파일제공 -> 웹 환경에서 사용 편리
    2. 문법 간단
    3. 컴은 한번에 한 작업만 가능 -> 멀티쓰레드 관련 구현 필요