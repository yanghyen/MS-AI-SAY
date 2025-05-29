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

export const { changeTxt } = myTxtSlice.actions;

export default myTxtSlice.reducer;
