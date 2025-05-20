import { useReducer } from "react";

const MyHookSec = () => {
    const doFlagGame = (curState, payload) => {
        return curState + "-" + payload.what + " " + payload.do;
    };

    const [history, setHistory] = useReducer(doFlagGame, "시작");
    return (
        <>
            <h1>{history}</h1>
            <button
                onClick={() => {
                    setHistory({what: "청기", do: "올려"});
                }}
            >
                청기올려
            </button>
            <button
                onClick={() => {
                    setHistory({what: "청기", do: "내려"});
                }}
            >
                청기내려
            </button>
            <button
                onClick={() => {
                    setHistory({what: "백기", do: "올려"});
                }}
            >
                백기올려
            </button>
            <button
                onClick={() => {
                    setHistory({what: "백기", do: "내려"});
                }}
            >
                백기내려
            </button>
        </>
    );
};

export default MyHookSec;
