import React, { useEffect, useRef, useState } from "react";

const DrawingArea = () => {
    const [beginXyInfo, setBeginXyInfo] = useState({ x: 0, y: 0 });
    const [drawMode, setDrawMode] = useState(false);
    const paper = useRef();
    const [pen, setPen] = useState();

    useEffect(() => {
        setPen(paper.current.getContext("2d"));
        return () => {};
    }, []);

    const drawStart = (e) => {
        setDrawMode(true);
        setBeginXyInfo({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY });
    };
    const draw = (e) => {
        if (drawMode) {
            const endXyInfo = {
                x: e.nativeEvent.offsetX,
                y: e.nativeEvent.offsetY,
            };
            pen.beginPath();
            pen.moveTo(beginXyInfo.x, beginXyInfo.y);
            pen.lineTo(endXyInfo.x, endXyInfo.y);
            pen.closePath();
            pen.stroke();
            setBeginXyInfo({ x: endXyInfo.x, y: endXyInfo.y });
        }
    };
    const drawEnd = () => {
        setDrawMode(false);
    };

    return (
        <canvas
            ref={paper}
            style={{ border: "black solid 3px" }}
            width={500}
            height={500}
            onMouseDown={drawStart}
            onMouseMove={draw}
            onMouseUp={drawEnd}
        />
    );
};

export default DrawingArea;
