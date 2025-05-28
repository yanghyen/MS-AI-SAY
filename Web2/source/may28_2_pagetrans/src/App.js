import { Route, Routes } from 'react-router-dom';
import './App.css';
import MyP1 from './pages/myP1/myP1';
import MyP2 from './pages/myP2/myP2';
import MyP3 from './pages/myP3/myP3';
import MyP4 from './pages/myP4/myP4';
import MyP5 from './pages/myP5/myP5';
import MyP6 from './pages/myP6/myP6';
import MyP7 from './pages/myP7/myP7';
import MyP8 from './pages/myP8/myP8';

function App() {
  // 첫 페이지 : path="/" or index
  // http://localhost:3000/p2.go -> MyP2 뜸
  // 없는 주소 : path="*"
  return (
    <Routes>
      <Route path="*" element={<MyP8 />} />
      <Route index element={<MyP1 />} />
      <Route path='/p2.go' element={<MyP2/>} />
      <Route path='/p3.go' element={<MyP3/>} />
      <Route path='/p4.go/:name/:price' element={<MyP4/>} />
      <Route path='/p5.go' element={<MyP5/>} />
      <Route path='/p6.go' element={<MyP6/>} />
      <Route path='/p7.go' element={<MyP7/>} />
      {/* <Route path='/p8.go' element={<MyP8/>} /> */}
    </Routes>
  );
}

export default App;
