# React Repeat Statement
### 반복문
-   기존 JS for/while문 가능
-   jQuery와 비교

    ```js
    // jQuery
    // arrr 차례대로 탐색
    // 하나 만날 때마다 콜백함수
    $.each(arrr, function (i, n) {});

    // react
    let arrr = [123, 345, 12311, 345];
    arrr.map((nn, ii) => {
        // nn: 값   ii: index 번호
        alert("ASDF");
    });
    ```

-   vanillaJs/jQuery : 파싱 -> 반복문 -> tr/td만들기 -> 존재하던 table에 append
-   react : 파싱 -> 반복문 -> tr/td만들어서 -> return된 값을 변수에 저장 -> 변수 사용

    ```js
    const MyRSSecond = () => {
        const [fav, setFav] = useState(["Jx", "rain", "love", "summer"]);

        const data = fav.map((v, i) => {
            return <div>{v}</div>;
        });
        const data = fav.map((v, i) => <div>{v}</div>)
        // 둘이 같음

        return <div>{data}</div>;
    };
    ```
### 배열 정렬
```js
const sortedSnacks = snack.sort((s1, s2) => {
    if (s1.name > s2.name) {
        return 1;   // 1은 오름차순, -1은 내림차순
    }
    return -1;
});
```
- 배열 추가
    - 배열[i] = ???
    - 배열.concat(???) : 추가된 배열을 리턴
- 배열 vs list
    - Python : list
    - JS : 배열
    - 배열은 append와 다르게 수정 불가
    - concat : 배열을 새로 만들어서 리턴