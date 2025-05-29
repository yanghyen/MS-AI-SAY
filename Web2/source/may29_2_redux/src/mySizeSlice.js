// state : 상태
// reducer : 상태+액션 입력받아서 새로운 상태 리턴(사실상 바꿔주는)하는 함수
// action : 액션
// slice : reducer + action

// rxslice
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    fontSize: 30,
};

const mySizeSlice = createSlice({
    name: "mssssssssss", // 어차피 이 이름으로 안 불러서 안 중요함
    initialState,
    reducers: {
        bigger: (curState) => {
            curState.fontSize += 10;
        },
        smaller: (cs) => {
            cs.fontSize -= 10;
        },
    },
});

export const { bigger, smaller } = mySizeSlice.actions;

export default mySizeSlice.reducer;
