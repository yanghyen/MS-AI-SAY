## CSS
- HTML DOM 객체에 디자인 입혀주는 디자인 언어  
    - 아무 효과 없는 <div>, <span> 사용
    - <div> : 줄바꿈 있음
    - <span> : 아무것도 없음
### 위치
1. .html 내부
2. 따로 .css 파일
3. DOM 객체 속성
    - ```<h4 style="background-color: violet;">메롱</h4>```
### CSSselector
- 문법(CSSselector) : HTML DOM 객체 선택에 사용, 다른 분야에서도 많이 사용
```html
CSSselector {
    속성명 : 값;
    속성명 : 값;
    ...
}
```
- 기본형
    - 태그명 : 그것들 다
        ```
        h1{
            color : aqua;
        }
        ```
    - #id : id가 그거인 거
        ```
        #CSSmd{
            color : palevioletred;
            background-color: beige;
        }

        <a id="CSSmd" href="../../Summary/CSS.md">이걸 참고행</a><br>
        ```
    - .class : class가 그거인 것들, 여러개 넣을 수도 있음
        ```
        .ccc{
            font-family: "궁서";
        }

        <h3 class="ccc ddd eee">태그명 : 그것들 다</h3>
        ```
- 조합형
    - 기본형, 기본형 , ... : 여러개 한꺼번에 선택
    - 기본형 기본형 ... : 포함관계 선택(div 속에 있는 h3 선택하기)
    - 기본형.class : 해당하는 class만 선택
    ```
    h1, h2{
        text-decoration: underline;
    }
    div h3{
        <h3>집에 가지마 베이베</h3>
        <h4>너에게 줄 선물이 여깄는데</h4>
    }
    ```
- 상태형
    - 기본형:상태
    ```
    /* 글자 클릭할 때 글자색 빨강으로 바뀜*/
    h4:active{
        color: red;
    }
    ```