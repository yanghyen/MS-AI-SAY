import React from 'react'
import { useParams } from 'react-router-dom'

const MyP4 = () => {
  const snack = useParams();  // 요청주소
  return (
    <>
        <div>MyP4</div>
        <div>{snack.name} - {snack.price}</div>
    </>
  )
}

export default MyP4