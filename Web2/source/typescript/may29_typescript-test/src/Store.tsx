import React from 'react'
import type {Address, Restaurant} from './model/restaurant';
// info:Restaurant라서 info가 Restaurant로 들어옴
interface OwnProps {
    info:Restaurant,
    changeAddress(address:Address):void // return값이 없어서 void
}
const Store:React.FC<OwnProps> = ({info, changeAddress}) => {
  return (
    <div>{info.name}</div>
  )
}

export default Store