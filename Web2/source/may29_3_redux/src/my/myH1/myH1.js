import React from 'react'
import {useSelector} from "react-redux";
const MyH1 = () => {
    const text = useSelector((s) => 
        s.mts.txt
    );
  return (
    <>
        <h1>{text}</h1>
    </>
  )
}

export default MyH1