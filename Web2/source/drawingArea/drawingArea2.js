import React, { useEffect, useRef, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:7890");

const DrawingArea2 = () => {
    const [beginXyInfo, setBeginXyInfo] = useState({ x: 0, y: 0 });
    const [drawMode, setDrawMode] = useState(false);
    const paper = useRef();

    useEffect(() => {
        const pen = paper.current.getContext("2d");
        socket.on("drawInfoSrv", (di) => {
            pen.beginPath();
            pen.moveTo(di.bx, di.by);
            pen.lineTo(di.ex, di.ey);
            pen.closePath();
            pen.stroke();
        });
        return () => {
            socket.off("drawInfoSrv");
        };
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
            const drawInfo = {
                bx: beginXyInfo.x,
                by: beginXyInfo.y,
                ex: endXyInfo.x,
                ey: endXyInfo.y,
            };
            socket.emit("drawInfoClnt", drawInfo);
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

export default DrawingArea2;
