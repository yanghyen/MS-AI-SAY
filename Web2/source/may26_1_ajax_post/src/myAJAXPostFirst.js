import React, { useState } from "react";
import axios from "axios";

const MyAJAXPostFirst = () => {
    const [xy, setXy] = useState({ x: "", y: "" });
    const [result, setResult] = useState({
        hap: "",
        cha: "",
        gob: "",
        moks: "",
    });
    const changeXY = (e) => {
        setXy({ ...xy, [e.target.name]: e.target.value });
    };

    const fd = new FormData();
    fd.append("x", xy.x); // fd.append("요청파라미터명", 값);
    fd.append("y", xy.y);

    const getResult = () => {
        // axios
        //     .get(`http://195.168.9.206:1717/calculator.get?x=${xy.x}&y=${xy.y}`)
        //     .then((res) => {
        //         setResult(res.data);
        //     });
        axios
            .post(`http://195.168.9.206:1717/calculator.post`, fd, {
                withCredentials: true,  // 보안 설정
            })
            .then((res) => {
                setResult(res.data);
            });
    };

   
    


    return (
        <>
            <h1>계산기</h1>
            x : <input value={xy.x} name="x" onChange={changeXY} />
            <br />
            y : <input value={xy.y} name="y" onChange={changeXY} />
            <br />
            <br />
            <button onClick={getResult}>계산</button>
            <hr />
            <h1>결과</h1>
            {result.hap} {result.cha} {result.gob} {result.moks}
            

        </>
    );
};

export default MyAJAXPostFirst;
