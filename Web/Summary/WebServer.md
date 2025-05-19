## Web Server
- Apache Tomcat으로 작업한 html 파일을 배포해보자
![](https://velog.velcdn.com/images/yanghyen/post/9df2aa13-d84b-46fe-9152-30e8fd14fe12/image.png)  
Tomcat을 쓸 때 포트번호를 수정해줘야 한다.
먼저 Server Shutdown Port는 -1에서 1로 바꿔준다.
그리고 HTTP/1.1 Connector Port는 8080에서 80으로 바꿔준다.
80으로 바꿔주는 건 두가지 이유가 있다.
1) 실전 지향(8080은 주로 테스트)
2) OracleDB가 8080 사용 중이라 충돌 방지

Apache Server를 실행하기 위해선   
![](https://velog.velcdn.com/images/yanghyen/post/02ad351f-af41-4b4c-9257-4d9d11970da7/image.png)  
시작 버튼을 누르면 뜨는 Configure Tomcat을 누르면 되는데, 설치 직후에는 권한이 없다는 경고 메세지가 뜬다.
![](https://velog.velcdn.com/images/yanghyen/post/abb6b9b4-d0cc-470f-a5d0-ca08e97e0ac3/image.png)  
그러면 Tomcat이 설치된 경로로 들어가서 한번 tomcat을 실행한 뒤에 Configure Tomcat을 누르면 잘 실행된다.  
![](https://velog.velcdn.com/images/yanghyen/post/f7bcef58-733e-44d2-a047-4059afdc6b1e/image.png)  
Service가 잘 실행되고 있슴다.  
![](https://velog.velcdn.com/images/yanghyen/post/159529b5-e8d6-4636-9c31-7fef0f476c89/image.png)  
정말로 잘 실행되고 있는지 확인하기 위해, 내 PC의 IP주소를 확인해줍니다.  
![](https://velog.velcdn.com/images/yanghyen/post/5398fc56-1582-4e65-930e-79a1f4a2fffe/image.png)  
브라우저에 이렇게 뜨면 성공!  
http://IP주소:포트/폴더명/파일명 이 기본인데, 포트번호 80과 ROOT폴더는 생략 가능하므로 브라우저에 내 IP주소만 입력하면 저 화면이 뜹니당.  
![](https://velog.velcdn.com/images/yanghyen/post/939d32b9-9e4e-4651-b299-c584920d8aa8/image.png)  
작업한 파일을   
```C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps``` 
로 옮겨두면 불러올 수 있슴다  
이제는 ROOT폴더가 아니니 폴더명/파일명을 추가해주면 내가 작업한 html 파일이 뜹니다!  
서버에 올렸으니 해당 주소를 다른 컴퓨터에서 입력해도 동일한 화면이 뜨겠죠?  
