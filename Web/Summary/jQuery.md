## jQuery
### 왜 씀?
1. DOM객체를 찾아가야 하는 불편함 
2. 같은 이벤트 여러군데 연결하려면 일일히 해야 되는 노가다
3. 문법이 길고 에러 잡기 힘듦
4. main이 따로 없어서 body의 load 이벤트(body에 있는 거 화면에 다 나오고나서)를 써야 됨
### 사용법
1. jQuery 사이트 들어가서 소스 복사해오기
2. jQuery.js 파일 만들어서 소스 붙여넣기
3. jQuery 사용할 파일에서 jQuery.js 불러오기
### 문법
- jQuery(선택자).이벤트(콜백함수);
- jQuery는 $로 줄여쓰기 가능
    - $(선택자).이벤트(콜백함수);
- 선택자
    - 기존 JS 내장객체 사용 가능
        - CSS 선택자
- 이벤트
    - 기존 JS의 onXXX에서 on만 제거 
```jQuery
$(function () {
    $("h1").dblclick(function abcd(){
        for (var i = 0; i < 5; i++) {
            alert("ㅋ");
        }
    });
});
```
- html은 인터프리터 언어로 순차적으로 한줄 씩 실행되기 때문에 겉에 main 지정해줘야 h1 생성 -> 함수 실행 됨

### event-driven programming
- 이벤트에 콜백함수 연결해서 진행