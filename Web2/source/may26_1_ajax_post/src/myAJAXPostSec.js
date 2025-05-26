import axios from "axios";
import React, { useRef, useState } from "react";

const MyAJAXPostSec = () => {
    const [photo, setPhoto] = useState({ title: "", photo:"" });
    const [result, setResult] = useState({ title: "" });
    const photoInput = useRef();    // file 타입 input은 value 안써서

    const changePhoto = (e) => {
        // setPhoto({ ...photo, [e.target.name]: e.target.value });
        // 파일 유효성 검사 : e.target.value
        // 파일 여러개 선택도 되고 객체 형태로 받아 : e.target.files[0]
        if (e.target.name === "photo") {
            setPhoto({ ...photo, [e.target.name]: e.target.files[0] });
        } else {
            setPhoto({ ...photo, [e.target.name]: e.target.value });
        }
    };
    const photoFD = new FormData();
    photoFD.append("title", photo.title);
    photoFD.append("photo", photo.photo);

    const uploadPhoto = () => {
        // 기존 방식으로는 파일 인코딩이 불가하니, 인코딩방식을 multipart/form-data 방식으로 바꿔야
        axios
            .post(`http://195.168.9.206:1717/photo.upload`, photoFD, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            })
            .then((res) => {
                setResult(res.data);
                setPhoto({title:"", photo:""});
                photoInput.current.value = "";
            });
    };
    return (
        <>
            제목 :{" "}
            <input value={photo.title} name="title" onChange={changePhoto} />
            <br />
            <br />
            사진 : <input ref={photoInput} type="file" name="photo" onChange={changePhoto} />
            <br />
            <br />
            <button onClick={uploadPhoto}>업로드</button>
            <h2>제목: {result.title}</h2>
            <h2>파일명: {result.photo}</h2>
        </>
    );
};

export default MyAJAXPostSec;
