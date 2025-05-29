import React, { useState } from "react";

const MyTest = () => {
    const [css, setCss] = useState({ fontSize: 30 });
    return (
        <>
            <button
                onClick={() => {
                    setCss({ fontSize: css.fontSize + 10 });
                }}
            >
                크게
            </button>
            <button
                onClick={() => {
                    setCss({ fontSize: css.fontSize - 10 });
                }}
            >
                작게
            </button>
            <h1 style={css}>ㅋㅋㅋㅋ</h1>
        </>
    );
};

export default MyTest;
