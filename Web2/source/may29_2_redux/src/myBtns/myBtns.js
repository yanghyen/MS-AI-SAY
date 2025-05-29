import React from "react";
import { useDispatch } from "react-redux";
import { bigger, smaller } from "../mySizeSlice";

// dispatcher : state를 바꿔줄 존재
const MyBtns = () => {
    const d = useDispatch();

    return (
        <>
            <button
                onClick={() => {
                    // d(slice쪽 reducer 함수 이름)
                    d(bigger());
                }}
            >
                크게
            </button>
            <button
                onClick={() => {
                    d(smaller());
                }}
            >
                작게
            </button>
        </>
    );
};

export default MyBtns;
