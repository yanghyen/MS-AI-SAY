import './App.css';
import BmiEvent from './event/bmiEvent';
import MyKeyEvent from './event/myKeyEvent';
import MyMouseEvent from './event/myMouseEvent';
import MyPopupMenu from './event/myPopupMenu';
import MyPopupMenu2 from './event/myPopupMenu2';
import MyResizeEvent from './event/myResizeEvent';
import MyHookFirst from './hook/myHookFirst';
import MyHookFourth from './hook/myHookFourth';
import MyHookSec from './hook/myHookSec';
import MyHookThird from './hook/myHookThird';
import MySocketClnt from './socket/mySocketClnt';

function App() {
  return (
    <>
      <BmiEvent />
      <br /><hr /><br />
      <MyMouseEvent />
      <br /><hr /><br />
      <MyPopupMenu />
      <br /><hr /><br />
      <MyKeyEvent />
      <br /><hr /><br />
      <MyHookFirst />
      <br /><hr /><br />
      <MyHookSec />
      <br /><hr /><br />
      <MyHookThird />
      <br /><hr /><br />
      <MyResizeEvent />
      <br /><hr /><br />
      <MyPopupMenu2 />
      <br /><hr /><br />
      <MyHookFourth />
      <br /><hr /><br />
      <MySocketClnt />
    </>
  );
}

export default App;
