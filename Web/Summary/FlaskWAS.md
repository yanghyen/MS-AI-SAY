## Flask WAS
### Web Server
- HTML/CSS 올려두면 사용자가 접속해서 사용하게 해주는 서버
### WAS(Web Application Server)
- Web Server + 프로그램 실행 가능
- flask : Python WAS 라이브러리
- 사용자가 요청하면 HTML, CSS 만들어주는 프로그램 <- WAS 필요
### 접속 허용 주소 및 포트
- Flask에선 접속허용주소를 app.run(여기) 여기에 작성
```py
if __name__ == "__main":
    app.run(
        "0.0.0.0",  # 접속허용주소
        1234,       # 포트번호
        debug=True  # 정보 출력 & 재시작
    )
```
- 내 IP주소도 내 컴
- localhost, 127.0.0.1도 내 컴
- well-known port : 이미 약속된 포트번호
### HTTP 통신
- 클라이언트가 서버에게 요청
- 서버는 그 요청에 대해 응답
- 요청
    - GET 방식 : 주소를 직접 입력. <a>  
        요청 param이 주소를 통해 전달
    - POST 방식 : form을 통해서     
        보안성 높음  
        요청 param이 내부적으로 전달
- request parameter : 클라이언트가 WAS로 보내는 정보
- form + button
    - form 속 button 누르면 action에 있는 쪽으로 요청 날려줌
    - input에 쓴 걸 reqParam으로 만들어서
    ```html
    <form action="http://195.168.9.180:1234/calculate.do">
        <input name="xxx"><br>  name이 변수명, 입력값이 값
        <input name="yyy"><br>
        <button>(=^._.^=)</button>
    </form>
    ```