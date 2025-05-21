import { useEffect, useState } from "react";
import io from "socket.io-client";

const MyEchoClient = () => {
    const [msg, setMsg] = useState("");
    const [socket, setSocket] = useState();

    useEffect(() => {
        setSocket(io("http://localhost:1717"));

        // socket.on("srvMsg", (msg2) => { 
        //     alert(msg2);
        //  });
        // React는 화면 전환 잦은 사이트 개발에 유리 + JS + VDOM => 비동기식 추구
        //      state 변경한 게 바로 반영 안되고, 수정 후 다음 렌더링에 반영됨

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

export default MyEchoClient;
