## File Upload
### html
- form이 편하지만 실제로는 안 씀
    - form 속에 있는 button/ submit타입 input/ image타입 input 누르면
    - form 속에 있는 input   
        - name을 reqParam변수명으로  
        - 내용을 전기신호로 바꿔서(인코딩)
    - action에 쓴 링크로 요청해줌
### 파일 업로드
1. reqParam이 주소에 실려가는 GET방식은 파일 표현 불가 -> POST여야 함
2. 글자는 인코딩 가능, 파일은 인코딩 불가 -> 인코딩 방식 바꿔야 함
    - ```<form action="주소" method="post" enctype="multipart/form-data">```
    1. 인코딩방식이 바뀌어서 오니  
     ```pip install python-multipart```
    2. 파일 저장될 폴더 확보(서버)
    - 지금 서버 못 쓰고, 프로젝트 자체를 서버에 업로드할 거니까
    - > 프로젝트에 폴더 만들고 상대경로 쓰자
- uuid : 네트워크 상에서 구별할 때 씀
### 통신
1. 동기식 통신
- 요청 보내놓고 서버의 응답이 올 때까지의 시간동안 멈춤(응답없음)
2. 비동기식 통신 <- fastapi
- 요청 보내놓고 서버의 응답이 올 때까지의 시간동안 안 멈추고 사용 가능
- 비동기식으로 놔두면 파일이 다 불러지지도 않았는데 다음 소스 실행됨 
    - 동기식으로 바꿔야 됨 