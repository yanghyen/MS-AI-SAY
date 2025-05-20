import { useReducer, useState } from "react";

const changeSecCss = (curState, payload) => {
    return {...curState, color: payload};
};

const MyHookThird = () => {
    const [firstCss, setFirstCss] = useState({
        backgroundColor: "red",
        color: "white",
    });
    const [secCss, setSecCss] = useReducer(changeSecCss, {
        backgroundColor: "yellow",
        color: "black",
    });

    // useEffect(() => {
    //   alert("ha");
    // }); // MyHookThird가 화면상 변화 생길 때 호출
    
    // useEffect(() => {
    //   alert("ha");
    // }, []); // MyHookThird 첫 렌더링 때

    // useEffect(() => {
    //     alert("ha");
    // }, [firstCss]); // MyHookThird 첫 렌더링 때 + firstCss 값 바뀔 때마다
    
    // useEffect(() => {
    //   alert("ha");      // 첫 렌더링 때
    
    //   return () => {    // MyHookThird 소멸자, 화면에서 사라질 때 
    //     alert("ke");
    //   };
    // }, []);
    

    return (
        <>
            <input
                style={firstCss}
                value={firstCss.color}
                onChange={(e) => {
                    setFirstCss({ ...firstCss, color: e.target.value });
                }}
            />
            <p />
            <input
                style={secCss}
                value={secCss.color}
                onChange={(e) => {
                    setSecCss(e.target.value);
                }}
            />
        </>
    );
};

export default MyHookThird;
