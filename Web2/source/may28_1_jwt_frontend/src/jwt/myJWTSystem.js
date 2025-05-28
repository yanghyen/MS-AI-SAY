import axios from "axios";
import { useState } from "react";

const MyJWTSystem = () => {
    const [menu, setMenu] = useState({ name: "", price: "" });
    const changemenu = (e) => {
        setMenu({ ...menu, [e.target.name]: e.target.value });
    };

    const reg = () => {
        axios
            .get(
                `http://195.168.9.206:1717/menu.reg?name=${menu.name}&price=${menu.price}`
            )
            .then((res) => {
                // sessionStorage : 브라우저 닫을 때까지 쓸 수 있는 공간
                // -> 다른 페이지에서도 사용 가능
                sessionStorage.setItem("myJWT", res.data.menuJWT);
                setMenu({ name: "", price: "" });
            })
            .catch((error) => {
                console.error(
                    "Error during registration:",
                    error.response || error
                );
                alert("으앙");
            });
    };

    const show = () => {
        axios
            .get(
                `http://195.168.9.206:1717/menu.get?token=${sessionStorage.getItem(
                    "myJWT"
                )}`
            )
            .then((res) => {
                alert(JSON.stringify(res.data));
            });
    };

    const del = () => {
        sessionStorage.removeItem("myJWT");
    };

    const update = () => {
        axios
            .get(
                `http://195.168.9.206:1717/menu.update?token=${sessionStorage.getItem(
                    "myJWT"
                )}`
            )
            .then((res) => {
                sessionStorage.setItem("myJWT", res.data.menuJWT);
            });
    };

    return (
        <div>
            메뉴명 :{" "}
            <input name="name" value={menu.name} onChange={changemenu} />
            <p />
            가격 :{" "}
            <input name="price" value={menu.price} onChange={changemenu} />
            <p />
            <button onClick={reg}>등록</button>
            <button onClick={show}>확인</button>
            <button onClick={del}>삭제</button>
            <button onClick={update}>갱신</button>
        </div>
    );
};

export default MyJWTSystem;
