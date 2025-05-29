import React from "react";
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
