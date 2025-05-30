import { useState } from "react";
import "./App.css";
import Store from "./Store";
import type { Address, Restaurant } from "./model/restaurant";
import BestMenu from "./BestMenu";

let data: Restaurant = {
    name: "seattle coffee",
    category: "cafe",
    address: {
        city: "seattle",
        detail: "somewhere",
        zipCode: 213123,
    },
    menu: [
        { name: "latte", price: 4000, category: "coffee" },
        { name: "스초생", price: 3000, category: "dessert" },
    ],
};

const App: React.FC = () => {
    const [myRestaurant, setMyRestaurant] = useState<Restaurant>(data);
    const changeAddress = (address: Address) => {
        setMyRestaurant({ ...myRestaurant, address: address });
    };
    const showBestMenuName = (name:string) => { 
      return name
     }

    return (
        <>
            <div className="App">
                <Store info={myRestaurant} changeAddress={changeAddress} />
                <BestMenu name="평양냉면" category="food" price={18000} showBestMenuName={showBestMenuName} />
            </div>
        </>
    );
};

export default App;
