import React, { useEffect } from "react";
import mdtmc from "./mdt.module.css";

const MyDesignThird = () => {
    useEffect(() => {
        const h = 180;
        const w = 80;
        const msg = `키 : ${h}cm, 몸무게 : ${w}kg`;
        alert(msg);
    }, []);

    return (
        <div className={`${mdtmc.c} ${mdtmc.bgc} ${mdtmc.f}`}>
            MyDesignThird
        </div>
    );
};

export default MyDesignThird;
