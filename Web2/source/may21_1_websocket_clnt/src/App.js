import './App.css';
import MyEchoClient2 from './socket/myEchoClient2';
import CatchMind from './socket/catchMind';

function App() {
  return (
    <>
      {/* <MyEchoClient /> */}
      <hr /><br />
      <MyEchoClient2 />
      <hr /><br />
      <CatchMind />
      <hr /><br />
    </>
  );
}

export default App;
