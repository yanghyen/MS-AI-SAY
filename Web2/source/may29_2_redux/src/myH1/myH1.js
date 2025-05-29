import React from "react";
import { useSelector } from "react-redux";

// subscriber : state 구독하는 존재
const MyH1 = () => {
    // (store객체) => store객체.store에써둔이름
    const sizeCSS = useSelector((st) => st.mss);
    return (
        <>
            <h1 style={sizeCSS}>hahaha</h1>
        </>
    );
};

export default MyH1;
