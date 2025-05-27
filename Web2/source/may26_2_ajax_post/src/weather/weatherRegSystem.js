import axios from "axios";
import React, { useRef, useState } from "react";

const WeatherRegSystem = () => {
    const iconInput = useRef();
    const [weather, setWeather] = useState({ desc: "", temp: "", icon: "" });
    const [result, setResult] = useState({
        result: "",
        desc: "",
        temp: "",
        icon: "",
    });
    const weatherFD = new FormData();

    const changeWeather = (e) => {
        if (e.target.name === "icon") {
            setWeather({ ...weather, [e.target.name]: e.target.files[0] });
        } else {
            setWeather({ ...weather, [e.target.name]: e.target.value });
        }
    };

    weatherFD.append("icon", weather.icon);
    weatherFD.append("desc", weather.desc);
    weatherFD.append("temp", weather.temp);

    const regResult = () => {
        axios
            .post(`http://195.168.9.206:1010/weather.reg`, weatherFD, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            })
            .then((res) => {
                setResult(res.data);
                setWeather({ desc: "", temp: "", icon: "" });
                iconInput.current.value = "";
            });
    };
    return (
        <>
            날씨 :{" "}
            <input value={weather.desc} name="desc" onChange={changeWeather} />
            <p />
            기온 :{" "}
            <input value={weather.temp} name="temp" onChange={changeWeather} />
            <p />
            이미지 :{" "}
            <input
                ref={iconInput}
                type="file"
                name="icon"
                onChange={changeWeather}
            />
            <p />
            <button onClick={regResult}>등록</button>
            <hr />
            <h2>등록 성공여부 : {result.result}</h2>
            <h2>등록한 날씨 : {result.desc}</h2>
            <h2>등록한 기온 : {result.temp}</h2>
            <h2>등록한 파일명 : {result.icon}</h2>
            <img
                src={`http://195.168.9.206:1010/weather.icon.get?icon=${result.icon}`}
                alt=""
            />
            <a
                href={`http://localhost:8888/weather.icon.get?icon=${regResult.icon}`}
            >
                다운받기{" "}
            </a>
        </>
    );
};

export default WeatherRegSystem;
