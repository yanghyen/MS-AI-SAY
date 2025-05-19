# react
- JS OOP 라이브러리
- 화면이 자주 바뀌는 사이트 개발에 유리
### Node.js
- Node.js
    - npm(Node Package Manager)
    - yarn : npm 같은 역할, 패키지 관리 및 실행 가능
- VSCode 확장 프로그램
    - ESLint : ES6 자동완성
    - ES7 + React/Re... : React 자동완성
    - Prettier : 소스 정렬
- 화살표 함수 자동완성 : **anfn**
    - 화살표 함수 변수에 저장하기 자동완성 : **nfn**
### 프로젝트 만들기
1. 프로젝트 만들 곳에 가서 cmd  
    - ```yarn create react-app 프로젝트명```
2. ```cd 프로젝트명```
3. ```yarn start```
- port번호 수정
    - src/package.json
    ```
    "scripts": {
    "start": "set PORT=9999 && react-scripts start",
    ```
### React VS jQuery
- React
    - VirtualDOM : 
    - 소스 -> VDOM -> 화면
    - VDOM의 변경사항만 화면에 렌더링 -> 특정 부분만 수정
    - 화면이 자주 바뀌는 사이트 개발에 유리
- vanillaJS / jQuery
    - html에서 특정 부분만 수정이 일어나지 않고 html 처음부터 끝까지 다시 렌더링
    - 화면 자주 바뀌면 힘듦
    - html 소스 -> 화면 
    - 화면이 잘 바뀌지 않는 사이트 개발에 유리
### OOP 장점
- 소스 재사용!!!
### 객체(Component) 만들기
- 객체(Component) 만들려면 -> 클래스
- react측에서 클래스보다는 함수형 Component를 권장하는 쪽으로 바뀜
- 단축어 : **rafce**
```js
const MyH1 = () => {
  return <h1>키키</h1>;     // html 아니고 JSX
};

export default MyH1;
```
### JSX(JavaScript Xml) 
- 무조건 하나가 리턴돼야 함
- DOM 객체
    - react는 무조건 DOM객체 풀세트 형태 -> <br></br>
    - 객체를 비워두고 싶거나 원래 풀세트 아닌 형태 -> <br />
- 속성 값 자리에 ```"값"```, ```{JS문법}```
    - {}에 ```anfn```으로 함수 넣기 
    ```js
    const MyTbl = () => {
        const showAlert = () => { 
            alert("haha");
        }
        
    return (
        <table border="1">
            <tr>
                <td>
                    <button onClick={showAlert}>버튼</button>
                </td>
            </tr>
        </table>
    )
    }

    export default MyTbl
    ```
- vanillaJS/jQuery : 버튼을 눌렀을 시점에 input에 적힌 내용 출력 
- React : state(상태, 속성에 해당)를 상시 업데이트
    - 버튼을 눌렀을 때 그 시점의 state를 출력하자
- OOP
    - 속성 : 멤버변수
    - 액션 : 메소드
- class를 만드려고 했으나, react측에서 함수 형태를 권장해서 함수를 만듦
    - 단순 함수에서 멤버변수/메소드 표현 불가
    - react측에서 hook이라는 걸 제공 
    - 멤버변수 느낌 : useState
    - const [멤버변수, setter] = useState(기본값)
        - setter : 멤버변수에 값 넣을 때 쓰는 함수
        - 단축어 : **snippet**
        - ```ee.target.value : $(this).val();```
        ```py
        class ColorChange:
            def __init__(self):
                self.color = "black"
            def setColor(self, c):
                self.color = c
        ```
        ```js
        const ColorChange = () => {
        const [color, setColor] = useState("black");   black
        const changeColor = (ee) => { setColor(ee.target.value); } 

        return (
            <div>
            <h1>(∩^o^)⊃━☆</h1>
            <input value={color} onChange={changeColor}/>
            </div>
            );
        };
        // 처음에 color에 들어있는 값은 black
        // setColor는 color의 값을 바꾸는 함수

        // ee.target.value : $(this).val();
        ```
- CSS
    - JS객체 형태로 씀
    - 속성명이 낙타체
### package.json
- cmd 명령어
- 포트 바꾸고 싶으면
    ```
    "scripts": {
    "start": "set PORT=9999 && react-scripts start",
    ```
### 객체 값 그대로 가져오기
- ...객체 : 그 객체 값들 그대로 가져오기(ES6)

### 테이블 추가
- jQuery
    - ```$("<td></td>").attr("align", "center").text("aa");```
- React
    - ```<td align="center">aa</td>```