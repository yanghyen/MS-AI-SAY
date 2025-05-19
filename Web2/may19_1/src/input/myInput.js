import { useState } from "react";

const MyInput = () => {
    const [txt, setTxt] = useState("asd");

    return (
        <div>
            <h1>{txt}</h1>
            <input 
                value={txt} // txt의 값을 input 내용에 연동
                onChange={(ee) => { // input 내용 바뀔 때마다
                    // ee.target 이벤트가 발생한 것
                    setTxt(ee.target.value);    // 바뀐 내용을 txt에 연동
                }}
            />
        </div>
    );
};

export default MyInput;
