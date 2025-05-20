import { useState } from "react";

const MyTbl = () => {
  // 멤버변수 느낌
  const [inputVall, setInputVall] = useState("ㅋ"); // 기본값으로 ㅋ을 넣어둠

  // 메소드 느낌
  const showAlert = () => {
    alert("haha");
  };

  const showInputVal = () => {
    alert(inputVall);
  };

  const keyUp = (e) => {
    // e.target : $(this)
    setInputVall(e.tartget.value);
  };

  return (
    <>
      <h1>(ToT)/~~~</h1>
      <table border="1">
        <tr>
          <td>
            <button onClick={showAlert}>alert 출력 버튼</button>
          </td>
        </tr>
        <tr>
          <input value={inputVall} onChange={keyUp} />
          <button onClick={showInputVal}>input에 쓴 거 출력</button>
        </tr>
      </table>
    </>
  );
};

export default MyTbl;
