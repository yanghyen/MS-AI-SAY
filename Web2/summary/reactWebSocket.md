# React Web Socket

### 웹 소켓 연결 (이전 방식)

1. public/index.html에 `<script src="http://localhost:8787/socket.io/socket.io.js"></script>` 추가
2. window.???로 사용
    - `window.io.connect("http://localhost:8787");`

### 웹 소켓 연결 (클라이언트 라이브러리 이용)

1. 소켓 클라이언트 라이브러리 설치
    - `yarn add socket.io-client@2`
    - public/index.html 처리 안 해도 됨
2. io 가져오기
    - `import io from "socket.io-client";`
3. 소켓 연결
    ```js
    useEffect(() => {
        io("http://localhost:8787");
    }, []);
    ```
