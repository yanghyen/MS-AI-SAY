import React from "react";
import { Link, useNavigate } from "react-router-dom";

const MyP1 = () => {
    const n = useNavigate(); // 클릭 말고 다른 이벤트로 이동하고 싶으면

    return (
        <>
            <div>MyP1</div>
            <Link to="/p4.go/몽쉘/500">p4로</Link>&nbsp;
            <Link to="/p4.go/촉촉한초코칩/5000">p4로</Link>
            <hr />
            <Link to="/p5.go?name=메롱&age=20">p5로</Link>&nbsp;
            <Link to="/p5.go?name=집&age=100">p5로</Link>
            <hr />
            <button
                onDoubleClick={() => {
                    n("/p6.go");
                    // n(-1);  // 뒤로
                }}
            >
                p6으로
            </button>
        </>
    );
};

export default MyP1;
