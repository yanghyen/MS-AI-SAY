import { useState } from "react";

const MywhSecond = () => {
    const [wh, setWh] = useState({ width: 200, height: 200 });

    const changeHeight = (e) => {
        // e.target.value 높이input에 쓴 내용
        // wh에서 width는 원래 값 그대로, height만 바꾸자
        setWh({ ...wh, height: e.target.value * 1 });
    };

    return (
        <>
            <table border={1} style={wh}>
                <tr>
                    <td>
                        <input
                            value={wh.width}
                            onChange={(e) => {
                                setWh({...wh,  width: e.target.value * 1});
                            }}
                        />
                    </td>
                </tr>
                <tr>
                    <td>
                        <input value={wh.height} onChange={changeHeight} />
                    </td>
                </tr>
            </table>
        </>
    );
};

export default MywhSecond;
