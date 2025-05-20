import React, { useState } from "react";

const MyKeyEvent = () => {
    const [eventinfo, setEventinfo] = useState("");
    const [keyinfo, setKeytinfo] = useState("");
    return (
        <>
            <input
                onKeyDown={(e) => {
                    setEventinfo("keyDown");
                    setKeytinfo(e.key);
                }}
                onKeyUp={(e) => {
                    setEventinfo("keyUp");
                    setKeytinfo(e.key);
                }}
            />
            <p />
            <h2>{eventinfo}</h2>
            <h2>{keyinfo}</h2>
        </>
    );
};

export default MyKeyEvent;
