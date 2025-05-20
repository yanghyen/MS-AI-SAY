// ColorChange에는 color 속성이 있고, 바꾸는 함수, 기본값이 black
// class ColorChange:
//     def __init__(self):
//         self.color = "black"
//     def setColor(self, c):
//         self.color = c

import { useState } from "react";

const ColorChange = () => {
    // const [color, setColor] = useState({ bg: "white", c: "black" }); 이거로는 어떻게 하는지 모르게씀
    const [letterColor, setColor] = useState("black");
    const [backColor, setBackColor] = useState("white");

    let go;
    let gogo;
    const changeColor = (ee) => {
        go = ee.target.value;
    };

    const changeBackColor = (ee) => {
        gogo = ee.target.value;
    };

    const changeH1Color = () => {
        setColor(go);
        setBackColor(gogo);
    };

    return (
        <div>
            <h1 style={{ color: letterColor, backgroundColor: backColor }}>
                (∩^o^)⊃━☆
            </h1>
            배경색 : <input onChange={changeBackColor} />
            <br />
            글자색 : <input onChange={changeColor} />
            <br />
            <button onClick={changeH1Color}>h1색깔바꾸기</button>
        </div>
    );
};

export default ColorChange;
