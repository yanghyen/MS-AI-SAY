import { useEffect, useState } from "react";

const MyPopupMenu2 = () => {
    const [popupCSS, setPopupCSS] = useState({
        position: "fixed",
        top: -100,
        left: -100,
        opacity: 0,
    });

    const summonPopup = (e) => {
        e.preventDefault(); // 우클릭했을 때 메뉴 뜨는 거 막음
    };

    const summonMyPopup = (e) => {
        if (e.button === 2) {
            setPopupCSS({
                ...popupCSS,
                top: e.clientY,
                left: e.clientX,
                opacity: 1,
            });
        }

        setTimeout(() => {
            setPopupCSS({
                ...popupCSS,
                top: -100,
                left: -100,
                opacity: 0,
            });
        }, 3000);
    };

    useEffect(() => {
        document.addEventListener("contextmenu", summonPopup);
        document.addEventListener("mouseup", summonMyPopup);

        return () => {
            document.removeEventListener("contextmenu", summonPopup);
            document.removeEventListener("mouseup", summonMyPopup);
        };
    },[]);

    return (
        <>
            <div style={popupCSS}>
                <table border={1}>
                    <tr>
                        <td>
                            <a href="https://www.naver.com">네이버로</a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href="https://www.naver.com">네이버로</a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href="https://www.naver.com">네이버로</a>
                        </td>
                    </tr>
                </table>
            </div>
        </>
    );
};

export default MyPopupMenu2;
