import axios from 'axios';

// JWT 확인
const MyP3 = () => {
    const show = () => {
        axios
            .get(
                `http://195.168.9.206:1717/menu.get?token=${sessionStorage.getItem(
                    "myJWT"
                )}`
            )
            .then((res) => {
                alert(JSON.stringify(res.data));
            });
    };

    return (
        <>
            <div>MyP3</div>
            <button onClick={show}>확인</button>
        </>
    );
};

export default MyP3;
