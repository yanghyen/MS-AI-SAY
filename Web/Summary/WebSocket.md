## Socket 통신
- http : 요청-응답
- socket : 실시간, 통신 채널
### Node.js
- 웹소켓서버 구현에 최적화
    1. js파일제공 -> 웹 환경에서 사용 편리
    2. 문법 간단
    3. 컴은 한번에 한 작업만 가능 -> 멀티쓰레드 관련 구현 필요

### 웹 소켓 라이브러리
- npm install socket.io@2
- socket.io의 최신 버전은 https만 지원해서 구버전 설치함
### 웹소켓 서비스 시작
```js
var io = require("socket.io")();
io.listen(9999);  // socket 통신 포트 번호
```
### 문법
- 객체(주어)
    - io.socekts : 연결된 모든 소켓들 
    - socket : 특정 소켓 하나
- 메소드(동사)
    - emit("제목", 내용) : 보낼 때
    - on("제목", 콜백함수) : 받을 때
    ```js
    io.sockets.emit("ASD", "zzz");
    socket.on("Asd", function(){
        // 정통 소켓통신 - 별개의 통신
        // 웹 소켓 - HTTP 통신
    });
    ```
