import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {configureStore} from "@reduxjs/toolkit";
import myTxtSlice from "./my/myTxtSlice";
import {Provider} from "react-redux";

// store에 등록된 slice만 사용 가능
const myTxtStore = configureStore({
  reducer: {
    mts : myTxtSlice  // mts로 불러서 씀
  }
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={myTxtStore}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
