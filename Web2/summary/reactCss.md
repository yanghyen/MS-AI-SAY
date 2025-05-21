# React CSS
- JS 객체 형태
- 낙타체
- 값이 숫자가 들어오면 단위 안 붙어도 됨
    - ```w={250}```
- 값이 글자로 들어오면 단위 붙어야 됨
    - ```width: props.w+"px"```
- 기존에 하던 css import하기
    - ```import './mct.css';```
    - import한 파일에만 적용되는 게 아니라 전체에 적용돼서 id, className 지정 잘해줘야 됨
### ???.module.css
- import를 안 한 파일에서도 className, id가 같으면 css가 적용됨 ㅠㅅㅠ
- 특정 프로젝트에만 적용하고 싶으면!
    - css 파일명을 ```???.module.css```
    - import "파일명" -> ```import 이름 from "파일명"```
    - ```className={이름.className}```으로 사용
    ```js
    import mds from "./mds.module.css";
    const MyDesignSec = () => {
        return (
            <>
                <div className='kekeke'>MDSㅋㅋㅋ</div>
                <div className={mds.hehehe}>MDSㅎㅎㅎ</div>
            </>
        );
    };
    ```
- ???.module.css인데 모든 프로젝트에 적용하고 싶으면 global 붙이면 됨
    ```js
    :global .ok {
        background-color: pink;
    }
    ```
### 클래스 여러개 적용하기
- ``으로 입력
    - ```<div className={`${mdtmc.c} ${mdtmc.bgc} ${mdtmc.f}`}>```