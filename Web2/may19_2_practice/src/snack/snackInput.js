import React, { useState } from "react";

const SnackBBS = () => {
    const [tempSnack, setTempSnack] = useState({ name: "", price: "" });
    const changeTempSnackName = (e) => { 
      setTempSnack({...tempSnack, name:e.target.value});
     }

    const reg = () => {
       alert(JSON.stringify(tempSnack));
       setTempSnack({name:"", price:""});
    };

    return (
        <div id="snackArea">
            이름{" "}
            <input
                id="nameInput"
                value={tempSnack.name}
                onChange={changeTempSnackName}
            />
            <br />
            가격{" "}
            <input
                id="priceInput"
                value={tempSnack.price}
                onChange={(e) => {
                  setTempSnack({...tempSnack, price:e.target.value});
                }}
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
            </table>
        </div>
    );
};

export default SnackBBS;
