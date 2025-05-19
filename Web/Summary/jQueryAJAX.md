## AJAX
- A : Asynchronous
- J : Javascript
- A : And
- X : Xml
    - 비동기식 통신을 통해서 JS로 XML 파싱
    - 브라우저의 동일출처정책에 의해 내 서버의 것만 받아올 수 있음
```html
$.ajax({
url : "주소(요청파라미터 빼고)",
data : {"변수명":값, "변수명":값, ...}
beforeSend : function(요청객체){
    요청객체.addRequestheader("이름","값");
    ...
},
success : function(받아온거){
    
    }
});
```
## Cross Domain AJAX
- 남의 데이터 가져오는 AJAX
- 서버 측에서 Access-Control-Allow-Origin 응답헤더 세팅하면 가져올 수 있음
- Proxy서버 : 한 단계 거쳐서
- form 안 쓰고 AJAX 쓰는 이유
    - 실시간 검색하려고
### 약식 버전(JSON만 가능)
```html
// 정식버전 AJAX - beforehand로 요청헤더 처리 가능
$.ajax({
     url: "https://api.openweathermap.org/data/2.5/weather",
     data: {
         lat: lat, lon: lon,
         appid: "baff8f3c6cbc28a4024e336599de28c4",
         units: "metric", lang: "kr"
     },
     success: function (asd) {
         alert(asd);
     }
 });

// JSON만 가능한 약식버전 AJAX - 요청헤더 처리 불가
var url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"lon="+lon+"appid="+"baff8f3c6cbc28a4024e336599de28c4"
$.getJSON(url, function(asd){
aler(asd);
});
```