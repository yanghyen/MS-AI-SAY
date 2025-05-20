import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const MyWSClnt2 = () => {
    const [socket, setSocket] = useState();
    useEffect(() => {
        setSocket(io("http://localhost:8787"));
    }, []);

    return <div onClick={() => {
      socket.emit("test", "ㅋ");
    }}
    >
      WSClnt2</div>;
};

export default MyWSClnt2;
