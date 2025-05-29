# React Redux
### Redux
- 
### 라이브러리
- ```yarn add @reduxjs/toolkit react-redux```
### slice
- state : 상태
- reducer : 상태+액션 입력받아서 새로운 상태 리턴(사실상 바꿔주는)하는 함수
- action : 액션
- slice : reducer + action
### 과정
1. slice 만들기
    - src/myTxtSlice.js
    - 단축키 ```rxslice```로 시작
    - 주의) ```export const {}```에 reducers 꼭 등록하기
    - src/myTxtSlice.js 생성
    ```js
    import { createSlice } from "@reduxjs/toolkit";

    const initialState = {
        txt: "ヾ(⌐■_■)ノ♪",
    };

    const myTxtSlice = createSlice({
        name: "merong",
        initialState,
        reducers: {
            changeTxt: (curState, action) => {
                // action.payload : dispatcher쪽에서 보내준 값
                curState.txt = action.payload;
            },
        },
    });
    ```
export const { changeTxt } = myTxtSlice.actions;
2. store 만들어서 slice 등록
    - store에 등록된 slice만 사용 가능
    - src/index.js
    ```js
    import {configureStore} from "@reduxjs/toolkit";
    import myTxtSlice from "./my/myTxtSlice";
    import {Provider} from "react-redux";

    // store에 등록된 slice만 사용 가능
    const myTxtStore = configureStore({
    reducer: {
        mts : myTxtSlice  // mts로 불러서 씀
    }
    });

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(
    <Provider store={myTxtStore}>
        <React.StrictMode>
        <App />
        </React.StrictMode>
    </Provider>
    );
    ```
3. dispatch 작업
    - dispatcher : state를 바꿔줄 존재
    - src/my/myInput.js 생성
    ```js
    import { useDispatch } from "react-redux";
    import { changeTxt } from "../myTxtSlice";

    const MyInput = () => {
        const d = useDispatch();

        return (
            <>
                내용 :{" "}
                <input
                    onChange={(e) => {
                        d(changeTxt(e.target.value));
                    }}
                />
            </>
        );
    };

    export default MyInput;
    ```
4. useSelector 불러와서 slice 사용하기
    - src/my/myH1.js 생성
    ```js
    import {useSelector} from "react-redux";
    const MyH1 = () => {
        const text = useSelector((s) => 
            s.mts.txt
        );
    return (
        <>
            <h1>{text}</h1>
        </>
    )
    }

    export default MyH1
    ```