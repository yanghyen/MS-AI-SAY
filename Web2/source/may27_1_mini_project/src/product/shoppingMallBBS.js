import axios from "axios";
import React, { useEffect, useRef, useState } from "react";
import "./shoppingMallBBS.css";


const ShoppingMallBBS = () => {
    const [product, setProduct] = useState({
        name: "",
        price: "",
        desc: "",
        image: "",
    });
    // result를 배열로 초기화 (상품 목록 저장용)
    const [result, setResult] = useState([]);
    const imageInput = useRef();

    useEffect(() => {
        getResult(); // 컴포넌트가 마운트될 때 한번 실행
    }, []);

    const changeProduct = (e) => {
        if (e.target.name === "image") {
            setProduct({ ...product, [e.target.name]: e.target.files[0] });
        } else {
            setProduct({ ...product, [e.target.name]: e.target.value });
        }
    };

    const regResult = () => {
        const fd = new FormData();
        fd.append("name", product.name);
        fd.append("price", product.price);
        fd.append("desc", product.desc);
        fd.append("image", product.image);

        console.log("Sending FormData:", product);

        axios
            .post(`http://195.168.9.206:1717/product.reg`, fd, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            })
            .then((res) => {
                console.log("Response:", res);
                alert(res.data.result || "등록 성공");
                setProduct({ name: "", price: "", desc: "", image: "" });
                imageInput.current.value = "";
                getResult();
            })
            .catch((error) => {
                console.error(
                    "Error during registration:",
                    error.response || error
                );
                alert("등록 실패 FE");
            });
    };

    const getResult = () => {
        axios
            .post(`http://195.168.9.206:1717/product.get`, null, {
                withCredentials: true,
            })
            .then((res) => {
                if (res.data.result === "조회성공") {
                    setResult(res.data.products); // products 배열 저장
                } else {
                    alert("상품 조회 실패");
                    setResult([]);
                }
            })
            .catch(() => {
                alert("상품 조회 실패");
                setResult([]);
            });
    };

    const deleResult = (name) => {
        if (!window.confirm(`정말 '${name}' 상품을 삭제하시겠습니까?`)) return;
        axios
            .post(
                `http://195.168.9.206:1717/product.dele`,
                { name },
                { 
                    headers: { "Content-Type": "application/json" },
                    withCredentials: true 
                }
            )
            .then((res) => {
                alert("삭제!");
                getResult();
            })
            .catch((error) => {
                console.error("삭제 실패:", error.response || error);
                alert("상품 삭제 실패");
            });
    };

    return (
        <div className="shopping-mall-bbs">
            <h1>상품등록</h1>
            이름 :{" "}
            <input value={product.name} name="name" onChange={changeProduct} />
            <p />
            가격 :{" "}
            <input
                value={product.price}
                name="price"
                onChange={changeProduct}
            />
            <p />
            설명 :{" "}
            <input value={product.desc} name="desc" onChange={changeProduct} />
            <p />
            사진 :{" "}
            <input
                ref={imageInput}
                type="file"
                name="image"
                onChange={changeProduct}
            />
            <p />
            <button onClick={regResult}>등록</button>
            <hr />
            <h2>조회 결과</h2>
            <table border={1}>
                <thead>
                    <tr>
                        <th>이미지</th>
                        <th>이름</th>
                        <th>가격</th>
                        <th>설명</th>
                    </tr>
                </thead>
                <tbody>
                    {result.length === 0 ? (
                        <tr>
                            <td colSpan={4} style={{ textAlign: "center" }}>
                                조회된 상품이 없습니다.
                            </td>
                        </tr>
                    ) : (
                        result.map((item, idx) => (
                            <tr key={idx}>
                                <td>
                                    <img
                                        src={`http://195.168.9.206:1717/product.get.img?image=${item.image}`}
                                        alt=""
                                        width={100}
                                        height={100}
                                        onClick={() => deleResult(item.name)}
                                    />
                                </td>
                                <td>{item.name}</td>
                                <td>{item.price}</td>
                                <td>{item.desc}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default ShoppingMallBBS;
