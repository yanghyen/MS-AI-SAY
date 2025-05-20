import React from "react";

const MyRSFirst = () => {
    const gogo = () => {
        let arrr = [123, 345, 12311, 345];
        arrr.map((nn, ii) => {
            alert(ii + " : " + nn);
        });
    };
    return <button onClick={gogo}>MyRSFirst</button>;
};

export default MyRSFirst;
