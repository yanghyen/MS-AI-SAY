import React from 'react'
import type {Restaurant} from './model/restaurant';
// info:Restaurant라서 info가 Restaurant로 들어옴
interface OwnProps {
    info:Restaurant
}
const Store:React.FC<OwnProps> = () => {
  return (
    <div>Store</div>
  )
}

export default Store