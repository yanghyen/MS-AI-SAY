import React, { useState } from "react";

const MyRSSecond = () => {
    const [fav, setFav] = useState(["Jx", "rain", "love", "summer"]);

    // const data = fav.map((v, i) => {
    //     return <div>{v}</div>;
    // });

    const data = fav.map((v, i) => <div>{v}</div>);

    return <div>{data}</div>;
};

export default MyRSSecond;
