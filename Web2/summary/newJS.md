# New JavaScript
### 변수
- JS는 변수 선언 및 재할당 방식이 Python과 다름
- 반복문 내 변수 선언 자제할 것
- 
```js
var a = 10;     // a라는 변수 만들고, 거기에 10 넣어라
a = 20;         // 이미 있는 변수 a를 20으로 바꿔라 

for (var i = 0; i < 5; i++) {
    var b = 30; // b라는 변수 만들고 30 할당
}

var b;
for (var i = 0; i < 5; i++) {
    b = 30;     // 즉 반복문 속에 변수 만드는 거 자제해야 됨
}
```
- let : 변수 선언 / 이미 있는 변수명으로 또 변수 선언 못하게 함
- const : 상수 선언
```js
var c = 10;
function test() {
    alert(c);
    var c = 20; // c라는 볕수를 만들고, 거기다 30 넣어라
                // 같은 이름으로 변수 또 만드는 게 안돼야 정상
                // JS는 고급언어라 허용해줌 -> 혼란
    alert(c);
};
```
- == / ===
    - == : 자료형 제외하고 동리한지 체크
    - === : 자료형까지 동일한지 체크

- 화살표 함수(arrow function)
    - JS는 함수명 안 써도 됨 -> 화살표 함수
    - 콜백함수 화살표 함수로 바꾸기
    ```js
    navigator.geolocation.getCurrentPosition(function (h){
        alert(JSON.stringify(h));
    });
    // =>
    navigator.geolocation.getCurrentPosition((h) => {
        alert(JSON.stringify(h));
    });
    ```
    - 일반 함수도 화살표 함수로 표현하고 변수에 저장해서 사용
    ```js
    function pringHap(i, j){
        alert(i + j);
    };
    printHap(1000, 2000);
    
    const printHap = (i, j) => {
        alert(i + j);
    }
    printHap(1000, 2000);

    const getHap = (k, l) => k + l; // k + l 리턴
    ```
