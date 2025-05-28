import axios from "axios";
import React, { useState } from "react";
import { Link } from "react-router-dom";

// JWT 등록
const MyP2 = () => {
    const [menu, setMenu] = useState({ name: "", price: "" });
    const changeMenu = (e) => {
        setMenu({ ...menu, [e.target.name]: e.target.value });
    };

    const reg = () => {
        axios
            .get(
                `http://195.168.9.206:1717/menu.reg?name=${menu.name}&price=${menu.price}`
            )
            .then((res) => {
                sessionStorage.setItem("myJWT", res.data.menuJWT);
                setMenu({ name: "", price: "" });
            });
    };

    return (
        <>
            <div>
                메뉴명 :{" "}
                <input name="name" value={menu.name} onChange={changeMenu} />
                <p />
                가격 :{" "}
                <input name="price" value={menu.price} onChange={changeMenu} />
                <p />
                <button onClick={reg}>등록</button>
            </div>
            <a href="/p3.go">p3으로</a>&nbsp;
            <Link to="/p3.go">p3으로!</Link>
        </>
    );
};

export default MyP2;
