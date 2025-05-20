import React, { useState } from 'react'

const MyRSFourth = () => {
    const [snack, setSnack] = useState([
        {name: "칙촉", price: 4000},
        {name: "사또밥", price: 4550},
        {name: "다이제", price: 8000},
    ]);

    const sortedSnacks = snack.sort((s1, s2) => {
        if (s1.name > s2.name) {
            return 1;   // 1은 오름차순, -1은 내림차순
        }
        return -1;
    });

    const snackTrs = sortedSnacks.map((s, i) => {
        return (
            <tr>
                <td>{s.name}</td>
                <td>{s.price}</td>
            </tr>
        )
    })
  return (
    <table border={1}>{snackTrs}</table>
  )
}

export default MyRSFourth