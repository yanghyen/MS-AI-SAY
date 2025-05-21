import { useEffect, useState } from "react";
import io from "socket.io-client";

// React의 state시스템으론 안됨
const socket = io("http://localhost:1717");

const MyEchoClient2 = () => {
    const [msg, setMsg] = useState("");

    useEffect(() => {
        socket.on("srvMsg", (msg2) => { 
            alert(msg2);
         });
        return () => {};
    }, []);

    
    
    const sendMsg = () => {
        socket.emit("clntMsg", msg);
        setMsg("");
    };
    

    return (
        <>
            <input
                value={msg}
                onChange={(e) => {
                    setMsg(e.target.value);
                }}
            />
            <button onClick={sendMsg}>전송</button>
        </>
    );
};

export default MyEchoClient2;
