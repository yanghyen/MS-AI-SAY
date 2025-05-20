import React, { useEffect, useState } from "react";

const MyResizeEvent = () => {
    const [wh, setWh] = useState({
        w: window.innerWidth,
        h: window.innerHeight, // vanillaJS에서 브라우저 사이즈
    });

    const updateWH = () => {
        setWh({
            w: window.innerWidth,
            h: window.innerHeight,
        });
    };

    useEffect(() => {
      window.addEventListener("resize", updateWH);// 소스로 이벤트 연결
      
      return () => {
          window.removeEventListener("resize", updateWH);// 소스로 이벤트 끊기
        
      }
    }, [])
    


    return (
        <>
            <h2>{wh.w}</h2>
            <h2>{wh.h}</h2>

        </>
    );
};

export default MyResizeEvent;
