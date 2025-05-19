import { useState } from "react";

const Kekeke = () => {
    const [csss, setCsss] = useState({
        color: "black",
        backgroundColor: "white",
    });

    const [c, setC] = useState("black");
    const [bgc, setBgc] = useState("white");

    const changeBgc = (e) => {
        setBgc(e.target.value);
    };

    const changeH1CSS = () => {
        setCsss({ color: c, backgroundColor: bgc });
    };

    return (
        <div>
            <h1 style={{ csss }}>Kekeke</h1>
            배경색 : <input value={bgc} onChange={changeBgc} />
            <br />
            글자색 :{" "}
            <input
                value={c}
                onChange={(e) => {
                    setC(e.target.value);
                }}
            />
            <br />
            <button onClick={changeH1CSS}>h1디자인바꾸기</button>
        </div>
    );
};

export default Kekeke;
