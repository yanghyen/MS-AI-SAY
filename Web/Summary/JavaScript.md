## JavaScript
- HTML에 이벤트 서포트하는 프로그래밍 언어
- 인터프리터 방식(웹 브라우저의 JS엔진이 기계어로 바꿔서 실행)

### 출력
- alert("경고창");      // 단순 출력용
- confirm("확인창")     // 확인 -> true, 최소 -> false 리턴
- prompt("입력창");      // 입력한 내용이 리턴

### 연산자
- 대부분 Python과 같은데 
```javascript
var a = 10;
var b = "g";
alert(a + b);   // 붙여서 글자로
alert(a * b);   // 안됨
a++;    // a += 1;
a--;    // a -= 1;
```

### 논리 연산자
- and : &&
- or : ||
- not : !

### 형 변환
```js
var e = 10;
var f = e + ""; // int -> str
var g = f * 1;  // str -> int
```

### 함수
1. 함수 정의
2. HTML DOM 객체의 onXXX속성에 연결
    - 작업형태 상 작업이 불편
    - 긴 문법 + 인터프리터 방식 -> 에러 잡기 최악 -> vanilla JS(순정 버전) 여전히 불편
    - jQuery라는 JS라이브러리가 나오면서 본격적으로 쓰기 시작
    - react/vue : 본격적으로 발전된 JS라이브러리
```js
function getHap(a, b) {
    return a + b;
}

var c = getHap(2, 5);
alert(c);
```

### 제어문(조건문, 반복문)
1. if (Python과 동일)
```js
var a = 10;
if (a > 5) {
    alert("5보다 큼");
} else if (a > 3) {
    alert("5보다는 작고 3보다는 큼");
} else {
    alert("해당없음")
}
```
2. switch
```js
var role = "DBP";
switch(role) {
    case "DBA":
        alert("전원관리");
        alert("사용자관리");
    case "DBP":
        alert("CRUD");
    default:
        alert("서비스 이용");
        break;
}
```
3. if VS switch
- if : 조건식 가능, 가독성 좋음
- switch : 조건식 불가, 값만 가능
    - break 없으면 나머지 실행문들 실행 -> 전략적으로 사용
    - 권한부여 같은 상황에서 switch가 유리

### 랜덤 뽑기(Math 클래스)
- ```Math.random() // 0.0 ~ 1.0 중 추출```
- ```Math.random() * 1000 // 0.0 ~ 1000 중 추출```

### 용어
- callback 함수 : 직접 호출하지 않고 이벤트에 연결해서 이벤트 발생 시 자동 호출되는 함수