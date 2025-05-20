import React, { useState } from "react";

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

export default MyHookFirst;
