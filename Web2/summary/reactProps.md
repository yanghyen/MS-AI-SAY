# React Props
### propertys(props)
- <MyInput name="이게" age="props">
```js
// myPropsFirst.js
const MyPropsFirst = (asd) => {
  return (
    <>
        <h2>{asd.namee}</h2>  
    </>
  );
};

// app.js
<MyPropsFirst namee="메롱"/>
```
- 단축어 : **rafcp**
    - porps 자료형 지정하게 해줌 
    ```js
    MyPropsSecond.propTypes = {
        namee : PropTypes.string.isRequired,   // ptsr
        pricee : PropTypes.number
    }
    ```
    - 근데 저 타입 안 따라도 에러는 안 남
    - isRequird : 자동완성 정도의 느낌
    - 나머지는 소스 가독성 수준
- app.js에서 입력한 값 받기
    ```js
    // myPropsThird.js
    const MyPropsThird = props => {
    return (
        <div>
            <h3>{props.children}</h3>
        </div>
    );
    };
    // app.js
    <MyPropsThird>hihi</MyPropsThird>
    ```