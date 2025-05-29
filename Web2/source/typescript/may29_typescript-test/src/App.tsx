import { useState } from 'react'
import './App.css'
import Store from './Store'
import type {Restaurant} from './model/restaurant';


let data:Restaurant = {
  name: "seattle coffee",
  category: "cafe",
  address: {
    city: "seattle",
    detail: "somewhere",
    zipCode: 213123
  },
  menu: [{name:"latte", price:4000, category:"coffee"}, {name:"스초생", price:3000, category:"dessert"}]
}

const App:React.FC = () => {
  const [myRestaurant, setMyRestaurant] = useState<Restaurant>(data)

  

  return (
    <>
      <div>
        <Store info={myRestaurant} />
      </div>
    </>
  )
}

export default App
