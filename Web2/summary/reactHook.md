# React Hook

### 객체(class)

-   속성(멤버변수)
-   액션(메소드)
-   객체가 만들어질 때 (생성자)

## Hook

-   React : JS OOP library + DOM
-   객체 만드려면 class 필요 -> react측에서 class보다 function 쪽 권장
    -   함수로는 멤버변수, 메소드, 생성자 표현 불가
    -   react 측에서 Hook이라는 걸 제공
-   useState : 멤버변수 + 멤버변수값 바꿀 수 있는 메소드(setter)
-   `const [멤버변수명, setter메소드명] = useState(기본값);`

```js
const MyHookFirst = () => {
    const [cnt, setCnt] = useState(0);
    return (
        <>
            <h1>{cnt}</h1>
            <button
                onClick={() => {
                    // cnt += 1;
                    setCnt(cnt + 1);
                }}
            >
                버튼
            </button>
        </>
    );
};
```

### 멤버변수 비슷한 거

-   useReducer : 멤버변수 + 멤버변수값 바꿀 수 있는 메소드 (setter)
    -   setter에 변화(단순히 바꾸기만 하는 거 이상의 것)
    -   정리효과
    -   `const [멤버변수, setter] = useReducer(함수, 기본값);`
    -   setter 호출하면 뒤에 쓴 함수 실행
    -   setter 역할 함수는 바깥에 별도로 정의
-   setter(setHistory) 호출 시 뒤에 함수(doFlagGame)가 실행
-   setter의 파라미터
    1. 기존 state값(curState) : history에 들어있던 값 "시작"
    2. setter 호출시 보내준 값(payload) : {what: "청기", do: "올려"}
    -   최종적으로 바뀔 state를 리턴

```js
const doFlagGame = (curState, payload) => {
    return curState + "-" + payload.what + " " + payload.do;
};

const [history, setHistory] = useReducer(doFlagGame, "시작");
return (
    <>
        <h1>{history}</h1>
        <button
            onClick={() => {
                setHistory({ what: "청기", do: "올려" });
            }}
        >
            청기올려
        </button>
        <button
            onClick={() => {
                setHistory({ what: "청기", do: "내려" });
            }}
        >
            청기내려
        </button>
        <button
            onClick={() => {
                setHistory({ what: "백기", do: "올려" });
            }}
        >
            백기올려
        </button>
        <button
            onClick={() => {
                setHistory({ what: "백기", do: "내려" });
            }}
        >
            백기내려
        </button>
    </>
);
```

### 생성자 비슷한 거

-   useEffect : 생성자, MyHookThird가 화면상 변화 생길 때 호출
    -   처음에 두번 뜨는 이유는 ../index.js에 <React.StrictMode> 때문
    -   strict 모드는 개발 과정 중에서 문제가 될 만한 함수를 두 번 실행하여 에러 잡는 걸 도와준다
    -   Double-Invoke 방식을 통해 알려주는 것
    -   여러 상황에서 발생할 수 있지만, 지금 상태에서 아는 건 useState 함수 뿐이다

```js
useEffect(() => {
    alert("ha");
}); // MyHookThird가 화면상 변화 생길 때 호출

useEffect(() => {
    alert("ha");
}, []); // MyHookThird 첫 렌더링 때

useEffect(() => {
    alert("ha");
}, [firstCss]); // MyHookThird 첫 렌더링 때 + firstCss 값 바뀔 때마다

useEffect(() => {
    alert("ha"); // 첫 렌더링 때

    return () => {
        // MyHookThird 소멸자, 화면에서 사라질 때
        alert("ke");
    };
}, []);
```

### React에서 canvas
- useRef : jQuery같은 선택