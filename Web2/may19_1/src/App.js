import './App.css';
import MyCssFirst from './css/myCssFirst';
import MyCssSecond from './css/myCssSecond';
import MyCssThird from './css/myCssThird';
import MyInput from './input/myInput';
import MyPropsFirst from './props/myPropsFirst';
import MyPropsSecond from './props/myPropsSecond';
import MyPropsThird from './props/myPropsThird';
import MyRSFirst from './repeatStmt/myRSFirst';
import MyRSFourth from './repeatStmt/myRSFourth';
import MyRSSecond from './repeatStmt/myRSSecond';
import MyRSThird from './repeatStmt/myRSThird';

function App() {
  return (
    <>
      <MyInput />
      <hr />
      <MyPropsFirst namee="메롱" ageee="13"/>
      <MyPropsSecond namee="빼빼로" pricee="3000"/>
      <MyPropsThird>hihi</MyPropsThird>
      <hr />
      <MyCssFirst bgc="pink" c="black" w="500" />
      <MyCssFirst bgc="green" c="beige" w="500" />
      <MyCssSecond />
      <hr />
      <MyCssThird />
      <hr />
      <MyRSFirst />
      <hr />
      <MyRSSecond />
      <hr />
      <MyRSThird />
      <hr />
      <MyRSFourth />
    </>
  );
}

export default App;
