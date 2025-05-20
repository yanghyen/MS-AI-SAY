import React, { useState } from "react";

const MyMouseEvent = () => {
    // const[멤버변수, setter] = useState(기본값);
    // 변수를 안 바꿀거면
    // const [divCss, setDivCss] = useState({width:200, height:200, border:"black solid 2px"})
    const divCss = { width: 200, height: 200, border: "black solid 2px" };
    const [moveInfo, setMoveInfo] = useState("");
    const [xyInfo, setXyInfo] = useState("");
    const [clickInfo, setClickInfo] = useState("");



    return (
        <>
            <div
                style={divCss}
                onMouseEnter={() => {
                    setMoveInfo("mouseEnter");
                }}
                onMouseMove={(e) => {
                  // html 기준 마우스 좌표 : e.clientX, e.clientY
                  // 객체 기준 마우스 좌표 : e.nativeEvent.offsetX, e.nativeEvent.offsetX 
                  // setXyInfo(e.clientX + ", " + e.clientY);
                  setXyInfo(e.nativeEvent.offsetX + ", " + e.nativeEvent.offsetY);
                }}
                onMouseLeave={() => {
                    setMoveInfo("mouseLeave");
                }}
                onMouseDown={(e) => { 
                  setClickInfo("mouseDown : " + e.button);
                 }}
                 onMouseUp={(e) => { 
                  setClickInfo("mouseUp : " + e.button);
                  }}
            ></div>
            <h2>{moveInfo}</h2>
            <h2>{xyInfo}</h2>
            <h2>{clickInfo}</h2>
        </>
    );
};

export default MyMouseEvent;
