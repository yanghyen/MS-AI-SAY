// 코드 체크

import { useEffect, useRef, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:1717");

const CatchMind = () => {
    const [beginXyInfo, setBeginXyInfo] = useState({ x: 0, y: 0 });
    const [drawMode, setDrawMode] = useState(false);
    const paper = useRef();

    
    
    // 소켓 수신: 서버에서 그림 정보 수신
    useEffect(() => {
        const pen = paper.current.getContext("2d");
        
        socket.on("srvMsg", (msg) => {
            pen.beginPath();
            pen.moveTo(msg.bx, msg.by);
            pen.lineTo(msg.ex, msg.ey);
            pen.closePath();
            pen.stroke();
        
        });
        
        return () => {
            socket.off("srvMsg");
        };
    }, []);
    
    // 마우스 드로잉 시작
    const drawStart = (e) => {
        setDrawMode(true);
        setBeginXyInfo({
            x: e.nativeEvent.offsetX,
            y: e.nativeEvent.offsetY,
        });
    };

    // 드로잉 중
    const draw = (e) => {
        if (drawMode) {
            const endXyInfo = {
                x: e.nativeEvent.offsetX,
                y: e.nativeEvent.offsetY,
            };
            const drawInfo = {
                bx:beginXyInfo.x, by:beginXyInfo.y,
                ex:endXyInfo.x, ey:endXyInfo.y
            };
            socket.emit("clntMsg", drawInfo);
            setBeginXyInfo({x:endXyInfo.x, y:endXyInfo.y});

        }
    };

    // 마우스 드로잉 끝
    const drawEnd = () => {
        setDrawMode(false);
    };

    return (
        <>
            <canvas
                ref={paper}
                width={300}
                height={300}
                style={{ backgroundColor: "green" }}
                onMouseDown={drawStart}
                onMouseMove={draw}
                onMouseLeave={drawEnd}
                onMouseUp={drawEnd}
            />
        </>
    );
};

export default CatchMind;
