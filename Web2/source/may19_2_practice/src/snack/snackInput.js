import React, { useState } from "react";
import "./snack.css";

// class
const SnackBBS = () => {
    // memberVar
    const [snacks, setSnacks] = useState([]);
    const snacksTr = snacks.map((snack, i) => {
        return (
            <tr className="dataTr" onClick={() => {
                del(snack.name);
            }}>
                <td align="center">{snack.name}</td>
                <td align="right">{snack.price}원</td>
            </tr>
        );
    });
    const [tempSnack, setTempSnack] = useState({ name: "", price: "" });

    // method
    const changeTempSnackName = (e) => {
        setTempSnack({ ...tempSnack, name: e.target.value });
    };

    const changeTempSnackPrice = (e) => {
        setTempSnack({ ...tempSnack, price: e.target.value });
    };

    const reg = () => {
        setSnacks(snacks.concat(tempSnack));
        setTempSnack({ name: "", price: "" });
    };

    const del = (name) => {
        // 칙촉을 지운다
        // 이름이 칙촉이 아닌 애들만 남긴다
        setSnacks(snacks.filter((snack) => snack.name !== name))
    };

    return (
        <div id="snackArea">
            이름{" "}
            <input
                class="inputTxt"
                value={tempSnack.name}
                onChange={changeTempSnackName}
            />
            <br />
            가격{" "}
            <input
                class="inputTxt"
                value={tempSnack.price}
                onChange={changeTempSnackPrice}
            />
            <br />
            <br />
            <button id="regBtn" onClick={reg}>
                등록
            </button>
            <hr />
            <table id="tempSnackTbl" border={1}>
                <tr>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
                {snacksTr}
            </table>
        </div>
    );
};

export default SnackBBS;
