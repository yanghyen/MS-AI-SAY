import React, { useState } from "react";

const MyRSThird = () => {
    const [nnn, setNnn] = useState([34, 2345, 567, 137357, 768]);

    // 배열 필터링
        // 배열 차례대로 탐색, 뭐 하나 만날 때마다 콜백함수
        // 콜백함수 속에서 조건문 써서 true값 리턴
    const nnn2 = nnn.filter((n) => n % 2 === 0)

    const marquees = nnn2.map((n, i) => (
        <marquee behavior="alternate">{n}</marquee>
    ));
    return <div>{marquees}</div>;
};

export default MyRSThird;
