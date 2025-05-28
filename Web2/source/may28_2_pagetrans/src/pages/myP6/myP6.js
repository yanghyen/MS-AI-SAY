import { Navigate } from "react-router-dom";

const MyP6 = () => {
    // redirect(강제이동)
    if (Math.random() > 0.5) {
        return <Navigate to="/p7.go" replace />;
    }
    return <div>MyP6</div>;
};

export default MyP6;
