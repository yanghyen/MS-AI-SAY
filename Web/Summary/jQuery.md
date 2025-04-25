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

### 반복문(for, for of, while)
- ```$(선택자).each(콜백함수);```
- DOM객체 탐색용
    ```html 
    // iii : index, vvv : value
    $("h1").each(function (iii, vvv) {
        alert(iii);
        alert(vvv);
    });
    ```
- JS배열 탐색용 -> JSON 파싱
    ```html
     var css = [
        {c:"pink", bgc:"black"},
        {c:"green", bgc:"#38190a"},
        {c:"baby pink", bgc:"#38190a"}
    ];
    $("h2").each(function(i, h2){
        $(h2).css("color", css[i].c);
        $(h2).css("background-color", css[i].bgc);
    });
    ```
### 선택한 객체에 대해서만 이벤트 적용하기
- this : 이벤트가 발생한 객체(콜밸함수를 호출한 대상)
```html
$("button").click(function () {
    $(this).css("background-color", "red");
});
```
- .parent() : 한단계 상위
- .closest("CSS선택자") : 상위로 올라가다가 가장 가까운 거
- .children() : 한단계 하위들
- .find("CSS선택자") : 하위로 내려가다가 가장 가까운 거
### 수정
- .text(바꿀거)
- .html(바꿀거)
- 바꿀거에 내용 없으면 그냥 내용 가져옴
### DOM객체 생성
- ```$("<button></button>")``` : 버튼 생성
- ```$("button")``` : 버튼 불러오기
### jQuery + VanillaJS
- jQuery를 써서 동적으로 추가된 DOM객체들의 이벤트 처리 
- 콜백함수에 값 전달